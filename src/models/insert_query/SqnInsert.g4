grammar SqnInsert;

// Common Lines Across All Lexers

// Value Handling

STRING: '"' (ESC | ~["\\])* '"' ;

fragment ESC: '\\' ["/\\bfnrt] | '\\u' HEX HEX HEX HEX ;

NUMBER: '-'? INT ('.' [0-9]+)? EXP? ;

fragment INT: '0' | [1-9] [0-9]* ;

fragment EXP: [eE] [+-]? [0-9]+ ;

fragment HEX: [0-9a-fA-F] ;

BOOLEAN: 'true' | 'false' ;

NULL: 'null' ;

// Whitespace Handling

WS: [ \t\r\n]+ -> skip ;

// Define Syntax For The Query Below
