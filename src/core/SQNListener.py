# Generated from SQN.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQNParser import SQNParser
else:
    from SQNParser import SQNParser

# This class defines a complete listener for a parse tree produced by SQNParser.
class SQNListener(ParseTreeListener):

    # Enter a parse tree produced by SQNParser#program.
    def enterProgram(self, ctx:SQNParser.ProgramContext):
        pass

    # Exit a parse tree produced by SQNParser#program.
    def exitProgram(self, ctx:SQNParser.ProgramContext):
        pass


    # Enter a parse tree produced by SQNParser#statement.
    def enterStatement(self, ctx:SQNParser.StatementContext):
        pass

    # Exit a parse tree produced by SQNParser#statement.
    def exitStatement(self, ctx:SQNParser.StatementContext):
        pass


    # Enter a parse tree produced by SQNParser#ddl.
    def enterDdl(self, ctx:SQNParser.DdlContext):
        pass

    # Exit a parse tree produced by SQNParser#ddl.
    def exitDdl(self, ctx:SQNParser.DdlContext):
        pass


    # Enter a parse tree produced by SQNParser#tableName.
    def enterTableName(self, ctx:SQNParser.TableNameContext):
        pass

    # Exit a parse tree produced by SQNParser#tableName.
    def exitTableName(self, ctx:SQNParser.TableNameContext):
        pass


    # Enter a parse tree produced by SQNParser#columnDef.
    def enterColumnDef(self, ctx:SQNParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by SQNParser#columnDef.
    def exitColumnDef(self, ctx:SQNParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by SQNParser#literal.
    def enterLiteral(self, ctx:SQNParser.LiteralContext):
        pass

    # Exit a parse tree produced by SQNParser#literal.
    def exitLiteral(self, ctx:SQNParser.LiteralContext):
        pass


    # Enter a parse tree produced by SQNParser#typeSpec.
    def enterTypeSpec(self, ctx:SQNParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by SQNParser#typeSpec.
    def exitTypeSpec(self, ctx:SQNParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by SQNParser#dml.
    def enterDml(self, ctx:SQNParser.DmlContext):
        pass

    # Exit a parse tree produced by SQNParser#dml.
    def exitDml(self, ctx:SQNParser.DmlContext):
        pass


    # Enter a parse tree produced by SQNParser#table_definition.
    def enterTable_definition(self, ctx:SQNParser.Table_definitionContext):
        pass

    # Exit a parse tree produced by SQNParser#table_definition.
    def exitTable_definition(self, ctx:SQNParser.Table_definitionContext):
        pass


    # Enter a parse tree produced by SQNParser#value_entries.
    def enterValue_entries(self, ctx:SQNParser.Value_entriesContext):
        pass

    # Exit a parse tree produced by SQNParser#value_entries.
    def exitValue_entries(self, ctx:SQNParser.Value_entriesContext):
        pass


    # Enter a parse tree produced by SQNParser#table_name.
    def enterTable_name(self, ctx:SQNParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SQNParser#table_name.
    def exitTable_name(self, ctx:SQNParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SQNParser#column_name.
    def enterColumn_name(self, ctx:SQNParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SQNParser#column_name.
    def exitColumn_name(self, ctx:SQNParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SQNParser#value.
    def enterValue(self, ctx:SQNParser.ValueContext):
        pass

    # Exit a parse tree produced by SQNParser#value.
    def exitValue(self, ctx:SQNParser.ValueContext):
        pass


    # Enter a parse tree produced by SQNParser#query.
    def enterQuery(self, ctx:SQNParser.QueryContext):
        pass

    # Exit a parse tree produced by SQNParser#query.
    def exitQuery(self, ctx:SQNParser.QueryContext):
        pass


    # Enter a parse tree produced by SQNParser#tableSelection.
    def enterTableSelection(self, ctx:SQNParser.TableSelectionContext):
        pass

    # Exit a parse tree produced by SQNParser#tableSelection.
    def exitTableSelection(self, ctx:SQNParser.TableSelectionContext):
        pass


    # Enter a parse tree produced by SQNParser#selectColumns.
    def enterSelectColumns(self, ctx:SQNParser.SelectColumnsContext):
        pass

    # Exit a parse tree produced by SQNParser#selectColumns.
    def exitSelectColumns(self, ctx:SQNParser.SelectColumnsContext):
        pass


    # Enter a parse tree produced by SQNParser#whereClause.
    def enterWhereClause(self, ctx:SQNParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SQNParser#whereClause.
    def exitWhereClause(self, ctx:SQNParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by SQNParser#condition.
    def enterCondition(self, ctx:SQNParser.ConditionContext):
        pass

    # Exit a parse tree produced by SQNParser#condition.
    def exitCondition(self, ctx:SQNParser.ConditionContext):
        pass


    # Enter a parse tree produced by SQNParser#predicate.
    def enterPredicate(self, ctx:SQNParser.PredicateContext):
        pass

    # Exit a parse tree produced by SQNParser#predicate.
    def exitPredicate(self, ctx:SQNParser.PredicateContext):
        pass


    # Enter a parse tree produced by SQNParser#operator.
    def enterOperator(self, ctx:SQNParser.OperatorContext):
        pass

    # Exit a parse tree produced by SQNParser#operator.
    def exitOperator(self, ctx:SQNParser.OperatorContext):
        pass


    # Enter a parse tree produced by SQNParser#columnName.
    def enterColumnName(self, ctx:SQNParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by SQNParser#columnName.
    def exitColumnName(self, ctx:SQNParser.ColumnNameContext):
        pass



del SQNParser