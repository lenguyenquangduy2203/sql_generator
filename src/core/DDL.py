# Generated from DDL.g4 by ANTLR 4.13.1
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
        4,1,37,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,
        2,4,6,8,0,2,1,0,1,7,1,0,8,13,38,0,10,1,0,0,0,2,22,1,0,0,0,4,34,1,
        0,0,0,6,36,1,0,0,0,8,38,1,0,0,0,10,11,3,2,1,0,11,12,5,16,0,0,12,
        17,3,4,2,0,13,14,5,19,0,0,14,16,3,4,2,0,15,13,1,0,0,0,16,19,1,0,
        0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,
        5,17,0,0,21,1,1,0,0,0,22,23,5,36,0,0,23,3,1,0,0,0,24,25,5,14,0,0,
        25,26,5,18,0,0,26,35,3,8,4,0,27,28,5,15,0,0,28,29,5,36,0,0,29,30,
        5,18,0,0,30,35,3,8,4,0,31,32,5,36,0,0,32,33,5,18,0,0,33,35,3,8,4,
        0,34,24,1,0,0,0,34,27,1,0,0,0,34,31,1,0,0,0,35,5,1,0,0,0,36,37,7,
        0,0,0,37,7,1,0,0,0,38,39,7,1,0,0,39,9,1,0,0,0,2,17,34
    ]

class DDL ( Parser ):

    grammarFileName = "DDL.g4"

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

    RULE_ddl = 0
    RULE_tableName = 1
    RULE_columnDef = 2
    RULE_literal = 3
    RULE_typeSpec = 4

    ruleNames =  [ "ddl", "tableName", "columnDef", "literal", "typeSpec" ]

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




    class DdlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(DDL.TableNameContext,0)


        def LPAREN(self):
            return self.getToken(DDL.LPAREN, 0)

        def columnDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DDL.ColumnDefContext)
            else:
                return self.getTypedRuleContext(DDL.ColumnDefContext,i)


        def RPAREN(self):
            return self.getToken(DDL.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DDL.COMMA)
            else:
                return self.getToken(DDL.COMMA, i)

        def getRuleIndex(self):
            return DDL.RULE_ddl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdl" ):
                listener.enterDdl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdl" ):
                listener.exitDdl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdl" ):
                return visitor.visitDdl(self)
            else:
                return visitor.visitChildren(self)




    def ddl(self):

        localctx = DDL.DdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ddl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.tableName()
            self.state = 11
            self.match(DDL.LPAREN)
            self.state = 12
            self.columnDef()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 13
                self.match(DDL.COMMA)
                self.state = 14
                self.columnDef()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(DDL.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DDL.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DDL.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = DDL.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(DDL.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PK(self):
            return self.getToken(DDL.PK, 0)

        def COLON(self):
            return self.getToken(DDL.COLON, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(DDL.TypeSpecContext,0)


        def FK(self):
            return self.getToken(DDL.FK, 0)

        def IDENTIFIER(self):
            return self.getToken(DDL.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DDL.RULE_columnDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDef" ):
                listener.enterColumnDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDef" ):
                listener.exitColumnDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDef" ):
                return visitor.visitColumnDef(self)
            else:
                return visitor.visitChildren(self)




    def columnDef(self):

        localctx = DDL.ColumnDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columnDef)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(DDL.PK)
                self.state = 25
                self.match(DDL.COLON)
                self.state = 26
                self.typeSpec()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(DDL.FK)
                self.state = 28
                self.match(DDL.IDENTIFIER)
                self.state = 29
                self.match(DDL.COLON)
                self.state = 30
                self.typeSpec()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(DDL.IDENTIFIER)
                self.state = 32
                self.match(DDL.COLON)
                self.state = 33
                self.typeSpec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(DDL.INT, 0)

        def FLOAT(self):
            return self.getToken(DDL.FLOAT, 0)

        def STRING(self):
            return self.getToken(DDL.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(DDL.BOOLEAN, 0)

        def DATE(self):
            return self.getToken(DDL.DATE, 0)

        def LONG(self):
            return self.getToken(DDL.LONG, 0)

        def NULL(self):
            return self.getToken(DDL.NULL, 0)

        def getRuleIndex(self):
            return DDL.RULE_literal

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

        localctx = DDL.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
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
            return self.getToken(DDL.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(DDL.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(DDL.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(DDL.BOOLEAN_TYPE, 0)

        def LONG_TYPE(self):
            return self.getToken(DDL.LONG_TYPE, 0)

        def DATE_TYPE(self):
            return self.getToken(DDL.DATE_TYPE, 0)

        def getRuleIndex(self):
            return DDL.RULE_typeSpec

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

        localctx = DDL.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
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





