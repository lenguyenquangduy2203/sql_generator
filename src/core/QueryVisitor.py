# Generated from Query.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Query import Query
else:
    from Query import Query

# This class defines a complete generic visitor for a parse tree produced by Query.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Query#query.
    def visitQuery(self, ctx:Query.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#tableSelection.
    def visitTableSelection(self, ctx:Query.TableSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#selectColumns.
    def visitSelectColumns(self, ctx:Query.SelectColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#whereClause.
    def visitWhereClause(self, ctx:Query.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#condition.
    def visitCondition(self, ctx:Query.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#predicate.
    def visitPredicate(self, ctx:Query.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#operator.
    def visitOperator(self, ctx:Query.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#value.
    def visitValue(self, ctx:Query.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#columnName.
    def visitColumnName(self, ctx:Query.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#tableName.
    def visitTableName(self, ctx:Query.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#literal.
    def visitLiteral(self, ctx:Query.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Query#typeSpec.
    def visitTypeSpec(self, ctx:Query.TypeSpecContext):
        return self.visitChildren(ctx)



del Query