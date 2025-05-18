# Generated from DML.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DML import DML
else:
    from DML import DML

# This class defines a complete listener for a parse tree produced by DML.
class DMLListener(ParseTreeListener):

    # Enter a parse tree produced by DML#dml.
    def enterDml(self, ctx:DML.DmlContext):
        pass

    # Exit a parse tree produced by DML#dml.
    def exitDml(self, ctx:DML.DmlContext):
        pass


    # Enter a parse tree produced by DML#table_definition.
    def enterTable_definition(self, ctx:DML.Table_definitionContext):
        pass

    # Exit a parse tree produced by DML#table_definition.
    def exitTable_definition(self, ctx:DML.Table_definitionContext):
        pass


    # Enter a parse tree produced by DML#value_entries.
    def enterValue_entries(self, ctx:DML.Value_entriesContext):
        pass

    # Exit a parse tree produced by DML#value_entries.
    def exitValue_entries(self, ctx:DML.Value_entriesContext):
        pass


    # Enter a parse tree produced by DML#table_name.
    def enterTable_name(self, ctx:DML.Table_nameContext):
        pass

    # Exit a parse tree produced by DML#table_name.
    def exitTable_name(self, ctx:DML.Table_nameContext):
        pass


    # Enter a parse tree produced by DML#column_name.
    def enterColumn_name(self, ctx:DML.Column_nameContext):
        pass

    # Exit a parse tree produced by DML#column_name.
    def exitColumn_name(self, ctx:DML.Column_nameContext):
        pass


    # Enter a parse tree produced by DML#value.
    def enterValue(self, ctx:DML.ValueContext):
        pass

    # Exit a parse tree produced by DML#value.
    def exitValue(self, ctx:DML.ValueContext):
        pass


    # Enter a parse tree produced by DML#literal.
    def enterLiteral(self, ctx:DML.LiteralContext):
        pass

    # Exit a parse tree produced by DML#literal.
    def exitLiteral(self, ctx:DML.LiteralContext):
        pass


    # Enter a parse tree produced by DML#typeSpec.
    def enterTypeSpec(self, ctx:DML.TypeSpecContext):
        pass

    # Exit a parse tree produced by DML#typeSpec.
    def exitTypeSpec(self, ctx:DML.TypeSpecContext):
        pass



del DML