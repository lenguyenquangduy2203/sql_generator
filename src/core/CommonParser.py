# Generated from CommonParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,9,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,2,1,0,1,
        7,1,0,8,13,6,0,4,1,0,0,0,2,6,1,0,0,0,4,5,7,0,0,0,5,1,1,0,0,0,6,7,
        7,1,0,0,7,3,1,0,0,0,0
    ]

class CommonParser ( Parser ):

    grammarFileName = "CommonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "'int'", 
                     "'float'", "'string'", "'boolean'", "'long'", "'date'", 
                     "'*'", "'@'", "'('", "')'", "':'", "','", "';'", "'?'", 
                     "'~'", "'and'", "'or'", "'between'", "'in'", "'like'", 
                     "'is'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'<<'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "STRING", "BOOLEAN", 
                      "DATE", "LONG", "NULL", "INT_TYPE", "FLOAT_TYPE", 
                      "STRING_TYPE", "BOOLEAN_TYPE", "LONG_TYPE", "DATE_TYPE", 
                      "PK", "FK", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "SEMI", "QUESTION", "TILDE", "AND", "OR", "BETWEEN", 
                      "IN", "LIKE", "IS", "EQ", "NEQ", "LT", "GT", "LE", 
                      "GE", "SLF", "IDENTIFIER", "WS" ]

    RULE_literal = 0
    RULE_typeSpec = 1

    ruleNames =  [ "literal", "typeSpec" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    STRING=3
    BOOLEAN=4
    DATE=5
    LONG=6
    NULL=7
    INT_TYPE=8
    FLOAT_TYPE=9
    STRING_TYPE=10
    BOOLEAN_TYPE=11
    LONG_TYPE=12
    DATE_TYPE=13
    PK=14
    FK=15
    LPAREN=16
    RPAREN=17
    COLON=18
    COMMA=19
    SEMI=20
    QUESTION=21
    TILDE=22
    AND=23
    OR=24
    BETWEEN=25
    IN=26
    LIKE=27
    IS=28
    EQ=29
    NEQ=30
    LT=31
    GT=32
    LE=33
    GE=34
    SLF=35
    IDENTIFIER=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CommonParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CommonParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CommonParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(CommonParser.BOOLEAN, 0)

        def DATE(self):
            return self.getToken(CommonParser.DATE, 0)

        def LONG(self):
            return self.getToken(CommonParser.LONG, 0)

        def NULL(self):
            return self.getToken(CommonParser.NULL, 0)

        def getRuleIndex(self):
            return CommonParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CommonParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(CommonParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(CommonParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(CommonParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(CommonParser.BOOLEAN_TYPE, 0)

        def LONG_TYPE(self):
            return self.getToken(CommonParser.LONG_TYPE, 0)

        def DATE_TYPE(self):
            return self.getToken(CommonParser.DATE_TYPE, 0)

        def getRuleIndex(self):
            return CommonParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = CommonParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





