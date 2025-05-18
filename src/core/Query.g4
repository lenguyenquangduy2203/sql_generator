parser grammar Query;

import CommonParser;

options { tokenVocab = CommonLexer; }

query: tableSelection (SEMI tableSelection)* whereClause?;

tableSelection: tableName TILDE selectColumns;

selectColumns: columnName (COMMA columnName)*;

whereClause: QUESTION condition;

condition: predicate| condition AND condition| condition OR condition| LPAREN condition RPAREN;

predicate: columnName operator value| columnName BETWEEN value AND value| columnName IN LPAREN value (COMMA value)* RPAREN| columnName LIKE STRING| columnName IS NULL;

operator: EQ | NEQ | LT | GT | LE | GE;

value: literal | columnName | LPAREN query RPAREN;

columnName: IDENTIFIER;

tableName: IDENTIFIER;