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
        return [model for stmt in ctx.statement() if (model := self.visit(stmt))]

    def visitDdl(self, ctx: DdlContext) -> DDLModel:
        table_name = ctx.tableName().IDENTIFIER().getText()
        columns = [self.visitColumnDef(c) for c in ctx.columnDef()]
        return DDLModel(table_name, columns)

    def visitColumnDef(self, ctx: ColumnDefContext) -> ColumnDef:
        col_name = self.columnDef.interpret(ctx)
        type_spec = self.visitTypeSpec(ctx.typeSpec())
        return ColumnDef(col_name, type_spec)

    def visitTypeSpec(self, ctx: TypeSpecContext) -> TypeSpec:
        return TypeSpec(self.typeSpec.interpret(ctx))

    def visitDml(self, ctx: DmlContext) -> DMLModel:
        definition = self.visitTable_definition(ctx.table_definition())
        entries = [self.visitValue_entries(e) for e in ctx.value_entries()]
        return DMLModel(definition, entries)

    def visitQuery(self, ctx: QueryContext) -> QueryModel:
        selections = dict(self.selections.interpret(sel) for sel in ctx.tableSelection())
        where_ctx = ctx.whereClause()
        condition = self.visitCondition(where_ctx.condition()) if where_ctx else None
        return QueryModel()  # Fill this out based on actual QueryModel implementation

    def visitTable_definition(self, ctx: Table_definitionContext) -> TableDefinition:
        name = ctx.table_name().IDENTIFIER().getText()
        columns = [c.IDENTIFIER().getText() for c in ctx.column_name()]
        return TableDefinition(name, columns)

    def visitValue_entries(self, ctx: Value_entriesContext) -> ValueEntry:
        return ValueEntry(ctx.value())

    def visitCondition(self, ctx: ConditionContext) -> Condition:
        return self.conditions.interpret(ctx, self)
