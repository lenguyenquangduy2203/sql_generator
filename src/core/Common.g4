lexer grammar Common;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

fragment DIGIT: [0-9];

INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT+;
STRING: '"' .*? '"';
BOOLEAN: 'true' | 'false';
DATE: DIGIT{4} '-' DIGIT{2} '-' DIGIT{2};
LONG: DIGIT+;

WS: [ \t\r\n]+ -> skip;

parser grammar CommonParser;

literal: INT | FLOAT | STRING | BOOLEAN | DATE | LONG | '(' query ')';

typeSpec: 'int' | 'float' | 'string' | 'boolean' | 'long' | 'date';
