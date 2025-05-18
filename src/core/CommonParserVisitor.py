# Generated from CommonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommonParser import CommonParser
else:
    from CommonParser import CommonParser

# This class defines a complete generic visitor for a parse tree produced by CommonParser.

class CommonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommonParser#literal.
    def visitLiteral(self, ctx:CommonParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommonParser#typeSpec.
    def visitTypeSpec(self, ctx:CommonParser.TypeSpecContext):
        return self.visitChildren(ctx)



del CommonParser