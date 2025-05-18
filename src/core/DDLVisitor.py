# Generated from DDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DDL import DDL
else:
    from DDL import DDL

# This class defines a complete generic visitor for a parse tree produced by DDL.

class DDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DDL#ddl.
    def visitDdl(self, ctx:DDL.DdlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DDL#tableName.
    def visitTableName(self, ctx:DDL.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DDL#columnDef.
    def visitColumnDef(self, ctx:DDL.ColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DDL#literal.
    def visitLiteral(self, ctx:DDL.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DDL#typeSpec.
    def visitTypeSpec(self, ctx:DDL.TypeSpecContext):
        return self.visitChildren(ctx)



del DDL