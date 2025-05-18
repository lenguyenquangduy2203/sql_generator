# Generated from Query.g4 by ANTLR 4.13.1
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
        4,1,37,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,3,0,34,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        5,2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,57,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,
        5,86,8,5,10,5,12,5,89,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,101,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,111,8,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,0,1,8,12,0,2,4,6,8,10,12,14,16,
        18,20,22,0,3,1,0,30,35,1,0,2,8,1,0,9,14,121,0,24,1,0,0,0,2,35,1,
        0,0,0,4,39,1,0,0,0,6,47,1,0,0,0,8,56,1,0,0,0,10,100,1,0,0,0,12,102,
        1,0,0,0,14,110,1,0,0,0,16,112,1,0,0,0,18,114,1,0,0,0,20,116,1,0,
        0,0,22,118,1,0,0,0,24,29,3,2,1,0,25,26,5,21,0,0,26,28,3,2,1,0,27,
        25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,33,1,0,0,
        0,31,29,1,0,0,0,32,34,3,6,3,0,33,32,1,0,0,0,33,34,1,0,0,0,34,1,1,
        0,0,0,35,36,3,18,9,0,36,37,5,23,0,0,37,38,3,4,2,0,38,3,1,0,0,0,39,
        44,3,16,8,0,40,41,5,20,0,0,41,43,3,16,8,0,42,40,1,0,0,0,43,46,1,
        0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,
        48,5,22,0,0,48,49,3,8,4,0,49,7,1,0,0,0,50,51,6,4,-1,0,51,57,3,10,
        5,0,52,53,5,17,0,0,53,54,3,8,4,0,54,55,5,18,0,0,55,57,1,0,0,0,56,
        50,1,0,0,0,56,52,1,0,0,0,57,66,1,0,0,0,58,59,10,3,0,0,59,60,5,24,
        0,0,60,65,3,8,4,4,61,62,10,2,0,0,62,63,5,25,0,0,63,65,3,8,4,3,64,
        58,1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,
        0,67,9,1,0,0,0,68,66,1,0,0,0,69,70,3,16,8,0,70,71,3,12,6,0,71,72,
        3,14,7,0,72,101,1,0,0,0,73,74,3,16,8,0,74,75,5,26,0,0,75,76,3,14,
        7,0,76,77,5,24,0,0,77,78,3,14,7,0,78,101,1,0,0,0,79,80,3,16,8,0,
        80,81,5,27,0,0,81,82,5,17,0,0,82,87,3,14,7,0,83,84,5,20,0,0,84,86,
        3,14,7,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,18,0,0,91,101,1,0,0,0,92,93,
        3,16,8,0,93,94,5,28,0,0,94,95,5,4,0,0,95,101,1,0,0,0,96,97,3,16,
        8,0,97,98,5,29,0,0,98,99,5,8,0,0,99,101,1,0,0,0,100,69,1,0,0,0,100,
        73,1,0,0,0,100,79,1,0,0,0,100,92,1,0,0,0,100,96,1,0,0,0,101,11,1,
        0,0,0,102,103,7,0,0,0,103,13,1,0,0,0,104,111,3,20,10,0,105,111,3,
        16,8,0,106,107,5,17,0,0,107,108,3,0,0,0,108,109,5,18,0,0,109,111,
        1,0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,111,15,1,
        0,0,0,112,113,5,1,0,0,113,17,1,0,0,0,114,115,5,1,0,0,115,19,1,0,
        0,0,116,117,7,1,0,0,117,21,1,0,0,0,118,119,7,2,0,0,119,23,1,0,0,
        0,9,29,33,44,56,64,66,87,100,110
    ]

class Query ( Parser ):

    grammarFileName = "Query.g4"

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

    RULE_query = 0
    RULE_tableSelection = 1
    RULE_selectColumns = 2
    RULE_whereClause = 3
    RULE_condition = 4
    RULE_predicate = 5
    RULE_operator = 6
    RULE_value = 7
    RULE_columnName = 8
    RULE_tableName = 9
    RULE_literal = 10
    RULE_typeSpec = 11

    ruleNames =  [ "query", "tableSelection", "selectColumns", "whereClause", 
                   "condition", "predicate", "operator", "value", "columnName", 
                   "tableName", "literal", "typeSpec" ]

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




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableSelection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Query.TableSelectionContext)
            else:
                return self.getTypedRuleContext(Query.TableSelectionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Query.SEMI)
            else:
                return self.getToken(Query.SEMI, i)

        def whereClause(self):
            return self.getTypedRuleContext(Query.WhereClauseContext,0)


        def getRuleIndex(self):
            return Query.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = Query.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.tableSelection()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 25
                self.match(Query.SEMI)
                self.state = 26
                self.tableSelection()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 32
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSelectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(Query.TableNameContext,0)


        def TILDE(self):
            return self.getToken(Query.TILDE, 0)

        def selectColumns(self):
            return self.getTypedRuleContext(Query.SelectColumnsContext,0)


        def getRuleIndex(self):
            return Query.RULE_tableSelection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSelection" ):
                listener.enterTableSelection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSelection" ):
                listener.exitTableSelection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSelection" ):
                return visitor.visitTableSelection(self)
            else:
                return visitor.visitChildren(self)




    def tableSelection(self):

        localctx = Query.TableSelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tableSelection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.tableName()
            self.state = 36
            self.match(Query.TILDE)
            self.state = 37
            self.selectColumns()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Query.ColumnNameContext)
            else:
                return self.getTypedRuleContext(Query.ColumnNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Query.COMMA)
            else:
                return self.getToken(Query.COMMA, i)

        def getRuleIndex(self):
            return Query.RULE_selectColumns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectColumns" ):
                listener.enterSelectColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectColumns" ):
                listener.exitSelectColumns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectColumns" ):
                return visitor.visitSelectColumns(self)
            else:
                return visitor.visitChildren(self)




    def selectColumns(self):

        localctx = Query.SelectColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectColumns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.columnName()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 40
                self.match(Query.COMMA)
                self.state = 41
                self.columnName()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(Query.QUESTION, 0)

        def condition(self):
            return self.getTypedRuleContext(Query.ConditionContext,0)


        def getRuleIndex(self):
            return Query.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = Query.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(Query.QUESTION)
            self.state = 48
            self.condition(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(Query.PredicateContext,0)


        def LPAREN(self):
            return self.getToken(Query.LPAREN, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Query.ConditionContext)
            else:
                return self.getTypedRuleContext(Query.ConditionContext,i)


        def RPAREN(self):
            return self.getToken(Query.RPAREN, 0)

        def AND(self):
            return self.getToken(Query.AND, 0)

        def OR(self):
            return self.getToken(Query.OR, 0)

        def getRuleIndex(self):
            return Query.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Query.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 51
                self.predicate()
                pass
            elif token in [17]:
                self.state = 52
                self.match(Query.LPAREN)
                self.state = 53
                self.condition(0)
                self.state = 54
                self.match(Query.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = Query.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        self.match(Query.AND)
                        self.state = 60
                        self.condition(4)
                        pass

                    elif la_ == 2:
                        localctx = Query.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        self.match(Query.OR)
                        self.state = 63
                        self.condition(3)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(Query.ColumnNameContext,0)


        def operator(self):
            return self.getTypedRuleContext(Query.OperatorContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Query.ValueContext)
            else:
                return self.getTypedRuleContext(Query.ValueContext,i)


        def BETWEEN(self):
            return self.getToken(Query.BETWEEN, 0)

        def AND(self):
            return self.getToken(Query.AND, 0)

        def IN(self):
            return self.getToken(Query.IN, 0)

        def LPAREN(self):
            return self.getToken(Query.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Query.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Query.COMMA)
            else:
                return self.getToken(Query.COMMA, i)

        def LIKE(self):
            return self.getToken(Query.LIKE, 0)

        def STRING(self):
            return self.getToken(Query.STRING, 0)

        def IS(self):
            return self.getToken(Query.IS, 0)

        def NULL(self):
            return self.getToken(Query.NULL, 0)

        def getRuleIndex(self):
            return Query.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = Query.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicate)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.columnName()
                self.state = 70
                self.operator()
                self.state = 71
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.columnName()
                self.state = 74
                self.match(Query.BETWEEN)
                self.state = 75
                self.value()
                self.state = 76
                self.match(Query.AND)
                self.state = 77
                self.value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.columnName()
                self.state = 80
                self.match(Query.IN)
                self.state = 81
                self.match(Query.LPAREN)
                self.state = 82
                self.value()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 83
                    self.match(Query.COMMA)
                    self.state = 84
                    self.value()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(Query.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.columnName()
                self.state = 93
                self.match(Query.LIKE)
                self.state = 94
                self.match(Query.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.columnName()
                self.state = 97
                self.match(Query.IS)
                self.state = 98
                self.match(Query.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(Query.EQ, 0)

        def NEQ(self):
            return self.getToken(Query.NEQ, 0)

        def LT(self):
            return self.getToken(Query.LT, 0)

        def GT(self):
            return self.getToken(Query.GT, 0)

        def LE(self):
            return self.getToken(Query.LE, 0)

        def GE(self):
            return self.getToken(Query.GE, 0)

        def getRuleIndex(self):
            return Query.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = Query.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Query.LiteralContext,0)


        def columnName(self):
            return self.getTypedRuleContext(Query.ColumnNameContext,0)


        def LPAREN(self):
            return self.getToken(Query.LPAREN, 0)

        def query(self):
            return self.getTypedRuleContext(Query.QueryContext,0)


        def RPAREN(self):
            return self.getToken(Query.RPAREN, 0)

        def getRuleIndex(self):
            return Query.RULE_value

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

        localctx = Query.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.literal()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.columnName()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(Query.LPAREN)
                self.state = 107
                self.query()
                self.state = 108
                self.match(Query.RPAREN)
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


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Query.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Query.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = Query.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(Query.IDENTIFIER)
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
            return self.getToken(Query.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Query.RULE_tableName

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

        localctx = Query.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(Query.IDENTIFIER)
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
            return self.getToken(Query.INT, 0)

        def FLOAT(self):
            return self.getToken(Query.FLOAT, 0)

        def STRING(self):
            return self.getToken(Query.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(Query.BOOLEAN, 0)

        def DATE(self):
            return self.getToken(Query.DATE, 0)

        def LONG(self):
            return self.getToken(Query.LONG, 0)

        def NULL(self):
            return self.getToken(Query.NULL, 0)

        def getRuleIndex(self):
            return Query.RULE_literal

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

        localctx = Query.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
            return self.getToken(Query.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(Query.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(Query.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(Query.BOOLEAN_TYPE, 0)

        def LONG_TYPE(self):
            return self.getToken(Query.LONG_TYPE, 0)

        def DATE_TYPE(self):
            return self.getToken(Query.DATE_TYPE, 0)

        def getRuleIndex(self):
            return Query.RULE_typeSpec

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

        localctx = Query.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




