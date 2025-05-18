# Generated from SQN.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQNParser import SQNParser
else:
    from SQNParser import SQNParser

# This class defines a complete generic visitor for a parse tree produced by SQNParser.

class SQNVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQNParser#program.
    def visitProgram(self, ctx:SQNParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#statement.
    def visitStatement(self, ctx:SQNParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#ddl.
    def visitDdl(self, ctx:SQNParser.DdlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#tableName.
    def visitTableName(self, ctx:SQNParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#columnDef.
    def visitColumnDef(self, ctx:SQNParser.ColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#literal.
    def visitLiteral(self, ctx:SQNParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#typeSpec.
    def visitTypeSpec(self, ctx:SQNParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#dml.
    def visitDml(self, ctx:SQNParser.DmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#table_definition.
    def visitTable_definition(self, ctx:SQNParser.Table_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#value_entries.
    def visitValue_entries(self, ctx:SQNParser.Value_entriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#table_name.
    def visitTable_name(self, ctx:SQNParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#column_name.
    def visitColumn_name(self, ctx:SQNParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#value.
    def visitValue(self, ctx:SQNParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#query.
    def visitQuery(self, ctx:SQNParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#tableSelection.
    def visitTableSelection(self, ctx:SQNParser.TableSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#selectColumns.
    def visitSelectColumns(self, ctx:SQNParser.SelectColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#whereClause.
    def visitWhereClause(self, ctx:SQNParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#condition.
    def visitCondition(self, ctx:SQNParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#predicate.
    def visitPredicate(self, ctx:SQNParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#operator.
    def visitOperator(self, ctx:SQNParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQNParser#columnName.
    def visitColumnName(self, ctx:SQNParser.ColumnNameContext):
        return self.visitChildren(ctx)



del SQNParser