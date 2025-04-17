# Generated from SqnCreate.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SqnCreateParser import SqnCreateParser
else:
    from SqnCreateParser import SqnCreateParser

# This class defines a complete generic visitor for a parse tree produced by SqnCreateParser.

class SqnCreateVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqnCreateParser#createQuery.
    def visitCreateQuery(self, ctx:SqnCreateParser.CreateQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#database.
    def visitDatabase(self, ctx:SqnCreateParser.DatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#databaseModifier.
    def visitDatabaseModifier(self, ctx:SqnCreateParser.DatabaseModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#table.
    def visitTable(self, ctx:SqnCreateParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#tableModifier.
    def visitTableModifier(self, ctx:SqnCreateParser.TableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#columnDef.
    def visitColumnDef(self, ctx:SqnCreateParser.ColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#columnType.
    def visitColumnType(self, ctx:SqnCreateParser.ColumnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqnCreateParser#columnConstraint.
    def visitColumnConstraint(self, ctx:SqnCreateParser.ColumnConstraintContext):
        return self.visitChildren(ctx)



del SqnCreateParser