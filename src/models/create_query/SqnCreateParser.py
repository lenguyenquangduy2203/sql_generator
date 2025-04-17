# Generated from SqnCreate.g4 by ANTLR 4.13.1
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
        4,1,39,141,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,3,0,22,8,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,37,8,1,10,1,12,1,40,9,1,1,1,1,1,
        3,1,44,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,57,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,70,8,3,10,3,12,
        3,73,9,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        87,8,3,10,3,12,3,90,9,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,111,8,5,10,5,12,5,114,9,
        5,1,5,1,5,3,5,118,8,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,139,8,7,1,7,0,0,8,0,2,4,6,
        8,10,12,14,0,3,1,0,14,16,3,0,10,10,19,20,35,35,2,0,24,28,35,35,149,
        0,16,1,0,0,0,2,25,1,0,0,0,4,56,1,0,0,0,6,58,1,0,0,0,8,93,1,0,0,0,
        10,95,1,0,0,0,12,121,1,0,0,0,14,138,1,0,0,0,16,17,5,1,0,0,17,18,
        5,2,0,0,18,21,5,3,0,0,19,22,3,2,1,0,20,22,3,6,3,0,21,19,1,0,0,0,
        21,20,1,0,0,0,22,23,1,0,0,0,23,24,5,4,0,0,24,1,1,0,0,0,25,26,5,1,
        0,0,26,27,5,5,0,0,27,28,5,3,0,0,28,43,5,35,0,0,29,30,5,6,0,0,30,
        31,5,7,0,0,31,32,5,3,0,0,32,33,5,8,0,0,33,38,3,4,2,0,34,35,5,6,0,
        0,35,37,3,4,2,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,9,0,0,42,44,1,0,0,0,
        43,29,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,4,0,0,46,3,1,0,
        0,0,47,57,5,10,0,0,48,57,5,11,0,0,49,50,5,1,0,0,50,51,5,12,0,0,51,
        52,5,3,0,0,52,53,5,13,0,0,53,54,7,0,0,0,54,57,5,4,0,0,55,57,5,35,
        0,0,56,47,1,0,0,0,56,48,1,0,0,0,56,49,1,0,0,0,56,55,1,0,0,0,57,5,
        1,0,0,0,58,59,5,1,0,0,59,60,5,17,0,0,60,61,5,3,0,0,61,76,5,35,0,
        0,62,63,5,6,0,0,63,64,5,7,0,0,64,65,5,3,0,0,65,66,5,8,0,0,66,71,
        3,8,4,0,67,68,5,6,0,0,68,70,3,8,4,0,69,67,1,0,0,0,70,73,1,0,0,0,
        71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,
        9,0,0,75,77,1,0,0,0,76,62,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,
        79,5,4,0,0,79,80,5,6,0,0,80,81,5,18,0,0,81,82,5,3,0,0,82,83,5,8,
        0,0,83,88,3,10,5,0,84,85,5,6,0,0,85,87,3,10,5,0,86,84,1,0,0,0,87,
        90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,
        0,91,92,5,9,0,0,92,7,1,0,0,0,93,94,7,1,0,0,94,9,1,0,0,0,95,96,5,
        1,0,0,96,97,5,21,0,0,97,98,5,3,0,0,98,99,5,35,0,0,99,100,5,6,0,0,
        100,101,5,22,0,0,101,102,5,3,0,0,102,117,3,12,6,0,103,104,5,6,0,
        0,104,105,5,23,0,0,105,106,5,3,0,0,106,107,5,8,0,0,107,112,3,14,
        7,0,108,109,5,6,0,0,109,111,3,14,7,0,110,108,1,0,0,0,111,114,1,0,
        0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,
        0,0,115,116,5,9,0,0,116,118,1,0,0,0,117,103,1,0,0,0,117,118,1,0,
        0,0,118,119,1,0,0,0,119,120,5,4,0,0,120,11,1,0,0,0,121,122,7,2,0,
        0,122,13,1,0,0,0,123,139,5,29,0,0,124,139,5,30,0,0,125,139,5,31,
        0,0,126,139,5,32,0,0,127,128,5,1,0,0,128,129,5,33,0,0,129,130,5,
        3,0,0,130,131,5,35,0,0,131,139,5,4,0,0,132,133,5,1,0,0,133,134,5,
        34,0,0,134,135,5,3,0,0,135,136,5,35,0,0,136,139,5,4,0,0,137,139,
        5,35,0,0,138,123,1,0,0,0,138,124,1,0,0,0,138,125,1,0,0,0,138,126,
        1,0,0,0,138,127,1,0,0,0,138,132,1,0,0,0,138,137,1,0,0,0,139,15,1,
        0,0,0,10,21,38,43,56,71,76,88,112,117,138
    ]

class SqnCreateParser ( Parser ):

    grammarFileName = "SqnCreate.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'\"create\"'", "':'", "'}'", "'\"database\"'", 
                     "','", "'\"modifiers\"'", "'['", "']'", "'\"if_not_exists\"'", 
                     "'\"cascade\"'", "'\"encoding\"'", "'UTF-'", "'8'", 
                     "'16'", "'32'", "'\"table\"'", "'\"columns\"'", "'\"temporary\"'", 
                     "'\"unlogged\"'", "'\"name\"'", "'\"type\"'", "'\"constraints\"'", 
                     "'\"int\"'", "'\"long\"'", "'\"string\"'", "'\"uuid\"'", 
                     "'\"datetime\"'", "'\"primary\"'", "'\"unique\"'", 
                     "'\"required\"'", "'\"auto_increment\"'", "'\"default\"'", 
                     "'\"reference\"'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "BOOLEAN", "NULL", "WS" ]

    RULE_createQuery = 0
    RULE_database = 1
    RULE_databaseModifier = 2
    RULE_table = 3
    RULE_tableModifier = 4
    RULE_columnDef = 5
    RULE_columnType = 6
    RULE_columnConstraint = 7

    ruleNames =  [ "createQuery", "database", "databaseModifier", "table", 
                   "tableModifier", "columnDef", "columnType", "columnConstraint" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    STRING=35
    NUMBER=36
    BOOLEAN=37
    NULL=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CreateQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def database(self):
            return self.getTypedRuleContext(SqnCreateParser.DatabaseContext,0)


        def table(self):
            return self.getTypedRuleContext(SqnCreateParser.TableContext,0)


        def getRuleIndex(self):
            return SqnCreateParser.RULE_createQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateQuery" ):
                listener.enterCreateQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateQuery" ):
                listener.exitCreateQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateQuery" ):
                return visitor.visitCreateQuery(self)
            else:
                return visitor.visitChildren(self)




    def createQuery(self):

        localctx = SqnCreateParser.CreateQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_createQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SqnCreateParser.T__0)
            self.state = 17
            self.match(SqnCreateParser.T__1)
            self.state = 18
            self.match(SqnCreateParser.T__2)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 19
                self.database()
                pass

            elif la_ == 2:
                self.state = 20
                self.table()
                pass


            self.state = 23
            self.match(SqnCreateParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatabaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def databaseModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqnCreateParser.DatabaseModifierContext)
            else:
                return self.getTypedRuleContext(SqnCreateParser.DatabaseModifierContext,i)


        def getRuleIndex(self):
            return SqnCreateParser.RULE_database

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatabase" ):
                listener.enterDatabase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatabase" ):
                listener.exitDatabase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatabase" ):
                return visitor.visitDatabase(self)
            else:
                return visitor.visitChildren(self)




    def database(self):

        localctx = SqnCreateParser.DatabaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_database)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(SqnCreateParser.T__0)
            self.state = 26
            self.match(SqnCreateParser.T__4)
            self.state = 27
            self.match(SqnCreateParser.T__2)
            self.state = 28
            self.match(SqnCreateParser.STRING)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 29
                self.match(SqnCreateParser.T__5)
                self.state = 30
                self.match(SqnCreateParser.T__6)
                self.state = 31
                self.match(SqnCreateParser.T__2)
                self.state = 32
                self.match(SqnCreateParser.T__7)
                self.state = 33
                self.databaseModifier()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 34
                    self.match(SqnCreateParser.T__5)
                    self.state = 35
                    self.databaseModifier()
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.match(SqnCreateParser.T__8)


            self.state = 45
            self.match(SqnCreateParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatabaseModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def getRuleIndex(self):
            return SqnCreateParser.RULE_databaseModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatabaseModifier" ):
                listener.enterDatabaseModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatabaseModifier" ):
                listener.exitDatabaseModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatabaseModifier" ):
                return visitor.visitDatabaseModifier(self)
            else:
                return visitor.visitChildren(self)




    def databaseModifier(self):

        localctx = SqnCreateParser.DatabaseModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_databaseModifier)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(SqnCreateParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(SqnCreateParser.T__10)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(SqnCreateParser.T__0)
                self.state = 50
                self.match(SqnCreateParser.T__11)
                self.state = 51
                self.match(SqnCreateParser.T__2)
                self.state = 52
                self.match(SqnCreateParser.T__12)
                self.state = 53
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.match(SqnCreateParser.T__3)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(SqnCreateParser.STRING)
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


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def columnDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqnCreateParser.ColumnDefContext)
            else:
                return self.getTypedRuleContext(SqnCreateParser.ColumnDefContext,i)


        def tableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqnCreateParser.TableModifierContext)
            else:
                return self.getTypedRuleContext(SqnCreateParser.TableModifierContext,i)


        def getRuleIndex(self):
            return SqnCreateParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable" ):
                return visitor.visitTable(self)
            else:
                return visitor.visitChildren(self)




    def table(self):

        localctx = SqnCreateParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(SqnCreateParser.T__0)
            self.state = 59
            self.match(SqnCreateParser.T__16)
            self.state = 60
            self.match(SqnCreateParser.T__2)
            self.state = 61
            self.match(SqnCreateParser.STRING)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 62
                self.match(SqnCreateParser.T__5)
                self.state = 63
                self.match(SqnCreateParser.T__6)
                self.state = 64
                self.match(SqnCreateParser.T__2)
                self.state = 65
                self.match(SqnCreateParser.T__7)
                self.state = 66
                self.tableModifier()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 67
                    self.match(SqnCreateParser.T__5)
                    self.state = 68
                    self.tableModifier()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(SqnCreateParser.T__8)


            self.state = 78
            self.match(SqnCreateParser.T__3)
            self.state = 79
            self.match(SqnCreateParser.T__5)
            self.state = 80
            self.match(SqnCreateParser.T__17)
            self.state = 81
            self.match(SqnCreateParser.T__2)
            self.state = 82
            self.match(SqnCreateParser.T__7)
            self.state = 83
            self.columnDef()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 84
                self.match(SqnCreateParser.T__5)
                self.state = 85
                self.columnDef()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(SqnCreateParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def getRuleIndex(self):
            return SqnCreateParser.RULE_tableModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableModifier" ):
                listener.enterTableModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableModifier" ):
                listener.exitTableModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableModifier" ):
                return visitor.visitTableModifier(self)
            else:
                return visitor.visitChildren(self)




    def tableModifier(self):

        localctx = SqnCreateParser.TableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tableModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34361312256) != 0)):
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


    class ColumnDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def columnType(self):
            return self.getTypedRuleContext(SqnCreateParser.ColumnTypeContext,0)


        def columnConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqnCreateParser.ColumnConstraintContext)
            else:
                return self.getTypedRuleContext(SqnCreateParser.ColumnConstraintContext,i)


        def getRuleIndex(self):
            return SqnCreateParser.RULE_columnDef

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

        localctx = SqnCreateParser.ColumnDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_columnDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SqnCreateParser.T__0)
            self.state = 96
            self.match(SqnCreateParser.T__20)
            self.state = 97
            self.match(SqnCreateParser.T__2)
            self.state = 98
            self.match(SqnCreateParser.STRING)
            self.state = 99
            self.match(SqnCreateParser.T__5)
            self.state = 100
            self.match(SqnCreateParser.T__21)
            self.state = 101
            self.match(SqnCreateParser.T__2)
            self.state = 102
            self.columnType()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 103
                self.match(SqnCreateParser.T__5)
                self.state = 104
                self.match(SqnCreateParser.T__22)
                self.state = 105
                self.match(SqnCreateParser.T__2)
                self.state = 106
                self.match(SqnCreateParser.T__7)
                self.state = 107
                self.columnConstraint()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 108
                    self.match(SqnCreateParser.T__5)
                    self.state = 109
                    self.columnConstraint()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(SqnCreateParser.T__8)


            self.state = 119
            self.match(SqnCreateParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def getRuleIndex(self):
            return SqnCreateParser.RULE_columnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnType" ):
                listener.enterColumnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnType" ):
                listener.exitColumnType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnType" ):
                return visitor.visitColumnType(self)
            else:
                return visitor.visitChildren(self)




    def columnType(self):

        localctx = SqnCreateParser.ColumnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34879832064) != 0)):
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


    class ColumnConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SqnCreateParser.STRING, 0)

        def getRuleIndex(self):
            return SqnCreateParser.RULE_columnConstraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnConstraint" ):
                listener.enterColumnConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnConstraint" ):
                listener.exitColumnConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnConstraint" ):
                return visitor.visitColumnConstraint(self)
            else:
                return visitor.visitChildren(self)




    def columnConstraint(self):

        localctx = SqnCreateParser.ColumnConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columnConstraint)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(SqnCreateParser.T__28)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(SqnCreateParser.T__29)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(SqnCreateParser.T__30)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(SqnCreateParser.T__31)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.match(SqnCreateParser.T__0)
                self.state = 128
                self.match(SqnCreateParser.T__32)
                self.state = 129
                self.match(SqnCreateParser.T__2)
                self.state = 130
                self.match(SqnCreateParser.STRING)
                self.state = 131
                self.match(SqnCreateParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.match(SqnCreateParser.T__0)
                self.state = 133
                self.match(SqnCreateParser.T__33)
                self.state = 134
                self.match(SqnCreateParser.T__2)
                self.state = 135
                self.match(SqnCreateParser.STRING)
                self.state = 136
                self.match(SqnCreateParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.match(SqnCreateParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





