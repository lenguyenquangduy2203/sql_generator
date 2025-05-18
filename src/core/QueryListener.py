# Generated from Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Query import Query
else:
    from Query import Query

# This class defines a complete listener for a parse tree produced by Query.
class QueryListener(ParseTreeListener):

    # Enter a parse tree produced by Query#query.
    def enterQuery(self, ctx:Query.QueryContext):
        pass

    # Exit a parse tree produced by Query#query.
    def exitQuery(self, ctx:Query.QueryContext):
        pass


    # Enter a parse tree produced by Query#tableSelection.
    def enterTableSelection(self, ctx:Query.TableSelectionContext):
        pass

    # Exit a parse tree produced by Query#tableSelection.
    def exitTableSelection(self, ctx:Query.TableSelectionContext):
        pass


    # Enter a parse tree produced by Query#selectColumns.
    def enterSelectColumns(self, ctx:Query.SelectColumnsContext):
        pass

    # Exit a parse tree produced by Query#selectColumns.
    def exitSelectColumns(self, ctx:Query.SelectColumnsContext):
        pass


    # Enter a parse tree produced by Query#whereClause.
    def enterWhereClause(self, ctx:Query.WhereClauseContext):
        pass

    # Exit a parse tree produced by Query#whereClause.
    def exitWhereClause(self, ctx:Query.WhereClauseContext):
        pass


    # Enter a parse tree produced by Query#condition.
    def enterCondition(self, ctx:Query.ConditionContext):
        pass

    # Exit a parse tree produced by Query#condition.
    def exitCondition(self, ctx:Query.ConditionContext):
        pass


    # Enter a parse tree produced by Query#predicate.
    def enterPredicate(self, ctx:Query.PredicateContext):
        pass

    # Exit a parse tree produced by Query#predicate.
    def exitPredicate(self, ctx:Query.PredicateContext):
        pass


    # Enter a parse tree produced by Query#operator.
    def enterOperator(self, ctx:Query.OperatorContext):
        pass

    # Exit a parse tree produced by Query#operator.
    def exitOperator(self, ctx:Query.OperatorContext):
        pass


    # Enter a parse tree produced by Query#value.
    def enterValue(self, ctx:Query.ValueContext):
        pass

    # Exit a parse tree produced by Query#value.
    def exitValue(self, ctx:Query.ValueContext):
        pass


    # Enter a parse tree produced by Query#columnName.
    def enterColumnName(self, ctx:Query.ColumnNameContext):
        pass

    # Exit a parse tree produced by Query#columnName.
    def exitColumnName(self, ctx:Query.ColumnNameContext):
        pass


    # Enter a parse tree produced by Query#tableName.
    def enterTableName(self, ctx:Query.TableNameContext):
        pass

    # Exit a parse tree produced by Query#tableName.
    def exitTableName(self, ctx:Query.TableNameContext):
        pass


    # Enter a parse tree produced by Query#literal.
    def enterLiteral(self, ctx:Query.LiteralContext):
        pass

    # Exit a parse tree produced by Query#literal.
    def exitLiteral(self, ctx:Query.LiteralContext):
        pass


    # Enter a parse tree produced by Query#typeSpec.
    def enterTypeSpec(self, ctx:Query.TypeSpecContext):
        pass

    # Exit a parse tree produced by Query#typeSpec.
    def exitTypeSpec(self, ctx:Query.TypeSpecContext):
        pass



del Query