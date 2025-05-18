# Generated from CommonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommonParser import CommonParser
else:
    from CommonParser import CommonParser

# This class defines a complete listener for a parse tree produced by CommonParser.
class CommonParserListener(ParseTreeListener):

    # Enter a parse tree produced by CommonParser#literal.
    def enterLiteral(self, ctx:CommonParser.LiteralContext):
        pass

    # Exit a parse tree produced by CommonParser#literal.
    def exitLiteral(self, ctx:CommonParser.LiteralContext):
        pass


    # Enter a parse tree produced by CommonParser#typeSpec.
    def enterTypeSpec(self, ctx:CommonParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by CommonParser#typeSpec.
    def exitTypeSpec(self, ctx:CommonParser.TypeSpecContext):
        pass



del CommonParser