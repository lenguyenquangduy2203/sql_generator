lexer grammar CommonLexer;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

fragment DIGIT: [0-9];

INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT+;
STRING: '"' .*? '"';
BOOLEAN: 'true' | 'false';
DATE: DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT;
LONG: DIGIT+;
NULL: 'null';

INT_TYPE: 'int';
FLOAT_TYPE: 'float';
STRING_TYPE: 'string';
BOOLEAN_TYPE: 'boolean';
LONG_TYPE: 'long';
DATE_TYPE: 'date';

PK: '*';
FK: '@';

LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';
SEMI: ';';
QUESTION: '?';
TILDE: '~';
AND: 'and';
OR: 'or';
BETWEEN: 'between';
IN: 'in';
LIKE: 'like';
IS: 'is';
EQ: '=';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
SLF: '<<';

WS: [ \t\r\n]+ -> skip;
