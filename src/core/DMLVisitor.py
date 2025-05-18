# Generated from DML.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DML import DML
else:
    from DML import DML

# This class defines a complete generic visitor for a parse tree produced by DML.

class DMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DML#dml.
    def visitDml(self, ctx:DML.DmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#table_definition.
    def visitTable_definition(self, ctx:DML.Table_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#value_entries.
    def visitValue_entries(self, ctx:DML.Value_entriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#table_name.
    def visitTable_name(self, ctx:DML.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#column_name.
    def visitColumn_name(self, ctx:DML.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#value.
    def visitValue(self, ctx:DML.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#literal.
    def visitLiteral(self, ctx:DML.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DML#typeSpec.
    def visitTypeSpec(self, ctx:DML.TypeSpecContext):
        return self.visitChildren(ctx)



del DML