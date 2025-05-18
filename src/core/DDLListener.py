# Generated from DDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DDL import DDL
else:
    from DDL import DDL

# This class defines a complete listener for a parse tree produced by DDL.
class DDLListener(ParseTreeListener):

    # Enter a parse tree produced by DDL#ddl.
    def enterDdl(self, ctx:DDL.DdlContext):
        pass

    # Exit a parse tree produced by DDL#ddl.
    def exitDdl(self, ctx:DDL.DdlContext):
        pass


    # Enter a parse tree produced by DDL#tableName.
    def enterTableName(self, ctx:DDL.TableNameContext):
        pass

    # Exit a parse tree produced by DDL#tableName.
    def exitTableName(self, ctx:DDL.TableNameContext):
        pass


    # Enter a parse tree produced by DDL#columnDef.
    def enterColumnDef(self, ctx:DDL.ColumnDefContext):
        pass

    # Exit a parse tree produced by DDL#columnDef.
    def exitColumnDef(self, ctx:DDL.ColumnDefContext):
        pass


    # Enter a parse tree produced by DDL#literal.
    def enterLiteral(self, ctx:DDL.LiteralContext):
        pass

    # Exit a parse tree produced by DDL#literal.
    def exitLiteral(self, ctx:DDL.LiteralContext):
        pass


    # Enter a parse tree produced by DDL#typeSpec.
    def enterTypeSpec(self, ctx:DDL.TypeSpecContext):
        pass

    # Exit a parse tree produced by DDL#typeSpec.
    def exitTypeSpec(self, ctx:DDL.TypeSpecContext):
        pass



del DDL