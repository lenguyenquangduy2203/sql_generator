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
        self.conditions = ConditionsInterpreter(self)

    def visit(self, tree) -> list[SQNModel]:
        return super().visit(tree)
    
    def visitDdl(self, ctx: DdlContext) -> DDLModel:
        table_name: str = ctx.tableName().IDENTIFIER().getText()
        columns: list[ColumnDef] = [self.visitColumnDef(col_ctx) for col_ctx in ctx.columnDef()]
        return DDLModel(table_name, columns)
    
    def visitDml(self, ctx: DmlContext) -> DMLModel:
        definition: TableDefinition = self.visitTable_definition(ctx.table_definition())
        entries: list[ValueEntry] = [self.visitValue_entries(val_ctx) for val_ctx in ctx.value_entries()]
        return DMLModel(definition, entries)
    
    def visitQuery(self, ctx: QueryContext) -> QueryModel:
        selections: dict[str, list[str]] = dict(self.selections.interpret(select_ctx) for select_ctx in ctx.tableSelection())
        where_ctx = ctx.whereClause()
        conditions: Condition | None = None
        if where_ctx:
            conditions = self.visitCondition(where_ctx.condition())

        return QueryModel(selections, conditions)
    
    def visitColumnDef(self, ctx: ColumnDefContext) -> ColumnDef:
        column_name: str = self.columnDef.interpret(ctx)
        type_spec: TypeSpec = self.visitTypeSpec(ctx.typeSpec())
        return ColumnDef(column_name, type_spec)
    
    def visitTypeSpec(self, ctx: TypeSpecContext) -> TypeSpec:
        name: str = self.typeSpec.interpret(ctx)
        return TypeSpec(name)
    
    def visitTable_definition(self, ctx: Table_definitionContext) -> TableDefinition:
        name: str = ctx.table_name().IDENTIFIER().getText()
        columns: list[str] = [col_ctx.IDENTIFIER().getText() for col_ctx in ctx.column_name()]
        return TableDefinition(name, columns)
    
    def visitValue_entries(self, ctx: Value_entriesContext) -> ValueEntry:
        return ValueEntry(ctx.value())
    
    def visitCondition(self, ctx: ConditionContext) -> Condition:
        return self.conditions.interpret(ctx)