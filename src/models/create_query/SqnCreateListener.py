# Generated from SqnCreate.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SqnCreateParser import SqnCreateParser
else:
    from SqnCreateParser import SqnCreateParser

# This class defines a complete listener for a parse tree produced by SqnCreateParser.
class SqnCreateListener(ParseTreeListener):

    # Enter a parse tree produced by SqnCreateParser#createQuery.
    def enterCreateQuery(self, ctx:SqnCreateParser.CreateQueryContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#createQuery.
    def exitCreateQuery(self, ctx:SqnCreateParser.CreateQueryContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#database.
    def enterDatabase(self, ctx:SqnCreateParser.DatabaseContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#database.
    def exitDatabase(self, ctx:SqnCreateParser.DatabaseContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#databaseModifier.
    def enterDatabaseModifier(self, ctx:SqnCreateParser.DatabaseModifierContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#databaseModifier.
    def exitDatabaseModifier(self, ctx:SqnCreateParser.DatabaseModifierContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#table.
    def enterTable(self, ctx:SqnCreateParser.TableContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#table.
    def exitTable(self, ctx:SqnCreateParser.TableContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#tableModifier.
    def enterTableModifier(self, ctx:SqnCreateParser.TableModifierContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#tableModifier.
    def exitTableModifier(self, ctx:SqnCreateParser.TableModifierContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#columnDef.
    def enterColumnDef(self, ctx:SqnCreateParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#columnDef.
    def exitColumnDef(self, ctx:SqnCreateParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#columnType.
    def enterColumnType(self, ctx:SqnCreateParser.ColumnTypeContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#columnType.
    def exitColumnType(self, ctx:SqnCreateParser.ColumnTypeContext):
        pass


    # Enter a parse tree produced by SqnCreateParser#columnConstraint.
    def enterColumnConstraint(self, ctx:SqnCreateParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by SqnCreateParser#columnConstraint.
    def exitColumnConstraint(self, ctx:SqnCreateParser.ColumnConstraintContext):
        pass



del SqnCreateParser