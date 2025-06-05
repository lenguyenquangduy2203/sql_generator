from src.application.ColumnDefInterpreter import ColumnDefInterpreter
from src.application.ConditionsInterpreter import ConditionsInterpreter
from src.application.SelectionsInterpreter import SelectionsInterpreter
from src.application.TypeSpecInterpreter import TypeSpecInterpreter
from src.core import (
    SQNVisitor, DdlContext, DmlContext, 
    Value_entriesContext, ConditionContext,
    QueryContext, ColumnDefContext, TypeSpecContext, 
    Table_definitionContext,
)
from src.core.contexts import ProgramContext
from src.models.abstractions import Condition, SQNModel
from src.models.ddl import DDLModel, ColumnDef, TypeSpec
from src.models.dml import DMLModel, TableDefinition, ValueEntry
from src.models.query import QueryModel


class SqlInterpreter(SQNVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.columnDef = ColumnDefInterpreter()
        self.typeSpec = TypeSpecInterpreter()
        self.selections = SelectionsInterpreter()
        self.conditions = ConditionsInterpreter()

    def visit(self, tree) -> list[SQNModel]:
        return super().visit(tree)
    
    def visitProgram(self, ctx: ProgramContext) -> list[SQNModel]:
        models = []
        for stmt in ctx.statement():
            model = self.visit(stmt)
            if model:
                models.append(model)
        return models

    def visitDdl(self, ctx: DdlContext) -> DDLModel:
        table_name: str = ctx.tableName().IDENTIFIER().getText()
        columns: list[ColumnDef] = [self.visitColumnDef(col_ctx) for col_ctx in ctx.columnDef()]
        return DDLModel(table_name, columns)

    def visitColumnDef(self, ctx: ColumnDefContext) -> ColumnDef:
        col_name = ctx.IDENTIFIER().getText() 
        type_spec = self.visitTypeSpec(ctx.typeSpec())
        return ColumnDef(col_name, type_spec)

    def visitTypeSpec(self, ctx: TypeSpecContext) -> TypeSpec:
        return TypeSpec(str(ctx.getText()) if hasattr(ctx, 'getText') else str(ctx))

    def visitDml(self, ctx: DmlContext) -> DMLModel:
        definition: TableDefinition = self.visitTable_definition(ctx.table_definition())
        entries: list[ValueEntry] = [self.visitValue_entries(val_ctx) for val_ctx in ctx.value_entries()]
        return DMLModel(definition, entries)
    
    def visitQuery(self, ctx: QueryContext) -> QueryModel:
        selections: dict[str, list[str]] = dict(self.selections.interpret(select_ctx) for select_ctx in ctx.tableSelection())
        where_ctx = ctx.whereClause()
        condition = self.visitCondition(where_ctx.condition()) if where_ctx else None
        return QueryModel(selections, condition)  # Fill this out based on actual QueryModel implementation
    
    def visitTable_definition(self, ctx: Table_definitionContext) -> TableDefinition:
        name: str = ctx.table_name().IDENTIFIER().getText()
        columns: list[str] = [col_ctx.IDENTIFIER().getText() for col_ctx in ctx.column_name()]
        return TableDefinition(name, columns)
    
    def visitValue_entries(self, ctx: Value_entriesContext) -> ValueEntry:
        return ValueEntry(ctx.value())
    
    def visitCondition(self, ctx: ConditionContext) -> Condition:
        return self.conditions.interpret(ctx, self)