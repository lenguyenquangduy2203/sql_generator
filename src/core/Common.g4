lexer grammar Common;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

fragment DIGIT: [0-9];

INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT+;
STRING: '"' .*? '"';
BOOLEAN: 'true' | 'false';
DATE: DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT;
LONG: DIGIT+;
NULL: 'null';

WS: [ \t\r\n]+ -> skip;

parser grammar CommonParser;

literal: INT | FLOAT | STRING | BOOLEAN | DATE | LONG | '(' query ')';

typeSpec: 'int' | 'float' | 'string' | 'boolean' | 'long' | 'date';
