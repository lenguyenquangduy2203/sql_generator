# Generated from DML.g4 by ANTLR 4.13.1
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
        4,1,37,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,1,1,1,1,1,1,1,1,1,5,
        1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,
        10,2,12,2,43,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,
        1,7,0,0,8,0,2,4,6,8,10,12,14,0,3,2,0,2,4,7,8,1,0,2,8,1,0,9,14,51,
        0,16,1,0,0,0,2,22,1,0,0,0,4,34,1,0,0,0,6,46,1,0,0,0,8,48,1,0,0,0,
        10,50,1,0,0,0,12,52,1,0,0,0,14,54,1,0,0,0,16,18,3,2,1,0,17,19,3,
        4,2,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,
        1,1,0,0,0,22,23,3,6,3,0,23,24,5,17,0,0,24,29,3,8,4,0,25,26,5,20,
        0,0,26,28,3,8,4,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,18,0,0,33,3,1,0,0,0,
        34,35,5,36,0,0,35,36,5,17,0,0,36,41,3,10,5,0,37,38,5,20,0,0,38,40,
        3,10,5,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,
        42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,18,0,0,45,5,1,0,0,0,46,47,5,
        1,0,0,47,7,1,0,0,0,48,49,5,1,0,0,49,9,1,0,0,0,50,51,7,0,0,0,51,11,
        1,0,0,0,52,53,7,1,0,0,53,13,1,0,0,0,54,55,7,2,0,0,55,15,1,0,0,0,
        3,20,29,41
    ]

class DML ( Parser ):

    grammarFileName = "DML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'null'", "'int'", "'float'", "'string'", "'boolean'", 
                     "'long'", "'date'", "'*'", "'@'", "'('", "')'", "':'", 
                     "','", "';'", "'?'", "'~'", "'and'", "'or'", "'between'", 
                     "'in'", "'like'", "'is'", "'='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'<<'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "INT", "FLOAT", "STRING", 
                      "BOOLEAN", "DATE", "LONG", "NULL", "INT_TYPE", "FLOAT_TYPE", 
                      "STRING_TYPE", "BOOLEAN_TYPE", "LONG_TYPE", "DATE_TYPE", 
                      "PK", "FK", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "SEMI", "QUESTION", "TILDE", "AND", "OR", "BETWEEN", 
                      "IN", "LIKE", "IS", "EQ", "NEQ", "LT", "GT", "LE", 
                      "GE", "SLF", "WS" ]

    RULE_dml = 0
    RULE_table_definition = 1
    RULE_value_entries = 2
    RULE_table_name = 3
    RULE_column_name = 4
    RULE_value = 5
    RULE_literal = 6
    RULE_typeSpec = 7

    ruleNames =  [ "dml", "table_definition", "value_entries", "table_name", 
                   "column_name", "value", "literal", "typeSpec" ]

    EOF = Token.EOF
    IDENTIFIER=1
    INT=2
    FLOAT=3
    STRING=4
    BOOLEAN=5
    DATE=6
    LONG=7
    NULL=8
    INT_TYPE=9
    FLOAT_TYPE=10
    STRING_TYPE=11
    BOOLEAN_TYPE=12
    LONG_TYPE=13
    DATE_TYPE=14
    PK=15
    FK=16
    LPAREN=17
    RPAREN=18
    COLON=19
    COMMA=20
    SEMI=21
    QUESTION=22
    TILDE=23
    AND=24
    OR=25
    BETWEEN=26
    IN=27
    LIKE=28
    IS=29
    EQ=30
    NEQ=31
    LT=32
    GT=33
    LE=34
    GE=35
    SLF=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DmlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_definition(self):
            return self.getTypedRuleContext(DML.Table_definitionContext,0)


        def value_entries(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DML.Value_entriesContext)
            else:
                return self.getTypedRuleContext(DML.Value_entriesContext,i)


        def getRuleIndex(self):
            return DML.RULE_dml

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDml" ):
                listener.enterDml(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDml" ):
                listener.exitDml(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDml" ):
                return visitor.visitDml(self)
            else:
                return visitor.visitChildren(self)




    def dml(self):

        localctx = DML.DmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dml)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.table_definition()
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.value_entries()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(DML.Table_nameContext,0)


        def LPAREN(self):
            return self.getToken(DML.LPAREN, 0)

        def column_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DML.Column_nameContext)
            else:
                return self.getTypedRuleContext(DML.Column_nameContext,i)


        def RPAREN(self):
            return self.getToken(DML.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DML.COMMA)
            else:
                return self.getToken(DML.COMMA, i)

        def getRuleIndex(self):
            return DML.RULE_table_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_definition" ):
                listener.enterTable_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_definition" ):
                listener.exitTable_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_definition" ):
                return visitor.visitTable_definition(self)
            else:
                return visitor.visitChildren(self)




    def table_definition(self):

        localctx = DML.Table_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_table_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.table_name()
            self.state = 23
            self.match(DML.LPAREN)
            self.state = 24
            self.column_name()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 25
                self.match(DML.COMMA)
                self.state = 26
                self.column_name()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(DML.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_entriesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLF(self):
            return self.getToken(DML.SLF, 0)

        def LPAREN(self):
            return self.getToken(DML.LPAREN, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DML.ValueContext)
            else:
                return self.getTypedRuleContext(DML.ValueContext,i)


        def RPAREN(self):
            return self.getToken(DML.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DML.COMMA)
            else:
                return self.getToken(DML.COMMA, i)

        def getRuleIndex(self):
            return DML.RULE_value_entries

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_entries" ):
                listener.enterValue_entries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_entries" ):
                listener.exitValue_entries(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_entries" ):
                return visitor.visitValue_entries(self)
            else:
                return visitor.visitChildren(self)




    def value_entries(self):

        localctx = DML.Value_entriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value_entries)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(DML.SLF)
            self.state = 35
            self.match(DML.LPAREN)
            self.state = 36
            self.value()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 37
                self.match(DML.COMMA)
                self.state = 38
                self.value()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(DML.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DML.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DML.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_name" ):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = DML.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(DML.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DML.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DML.RULE_column_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_name" ):
                listener.enterColumn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_name" ):
                listener.exitColumn_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_name" ):
                return visitor.visitColumn_name(self)
            else:
                return visitor.visitChildren(self)




    def column_name(self):

        localctx = DML.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_column_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(DML.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DML.STRING, 0)

        def INT(self):
            return self.getToken(DML.INT, 0)

        def FLOAT(self):
            return self.getToken(DML.FLOAT, 0)

        def LONG(self):
            return self.getToken(DML.LONG, 0)

        def NULL(self):
            return self.getToken(DML.NULL, 0)

        def getRuleIndex(self):
            return DML.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = DML.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 412) != 0)):
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(DML.INT, 0)

        def FLOAT(self):
            return self.getToken(DML.FLOAT, 0)

        def STRING(self):
            return self.getToken(DML.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(DML.BOOLEAN, 0)

        def DATE(self):
            return self.getToken(DML.DATE, 0)

        def LONG(self):
            return self.getToken(DML.LONG, 0)

        def NULL(self):
            return self.getToken(DML.NULL, 0)

        def getRuleIndex(self):
            return DML.RULE_literal

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

        localctx = DML.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 508) != 0)):
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
            return self.getToken(DML.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(DML.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(DML.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(DML.BOOLEAN_TYPE, 0)

        def LONG_TYPE(self):
            return self.getToken(DML.LONG_TYPE, 0)

        def DATE_TYPE(self):
            return self.getToken(DML.DATE_TYPE, 0)

        def getRuleIndex(self):
            return DML.RULE_typeSpec

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

        localctx = DML.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
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





