grammar SqnCreate;

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

createQuery: '{' '"create"' ':' (database | table) '}' ;

database: '{' '"database"' ':' STRING (',' '"modifiers"' ':' '[' databaseModifier (',' databaseModifier)* ']')? '}' ;

databaseModifier: '"if_not_exists"' | '"cascade"' | '{' '"encoding"' ':' 'UTF-' ('8' | '16' | '32') '}'  | STRING ;

table: '{' '"table"' ':' STRING (',' '"modifiers"' ':' '[' tableModifier (',' tableModifier)* ']')? '}' ',' '"columns"' ':' '[' columnDef (',' columnDef)* ']' ;

tableModifier: '"if_not_exists"' | '"temporary"' | '"unlogged"' | STRING ;

columnDef: '{' '"name"' ':' STRING ',' '"type"' ':' columnType (',' '"constraints"' ':' '[' columnConstraint (',' columnConstraint)* ']')? '}' ;

columnType: '"int"' | '"long"' | '"string"' | '"uuid"' | '"datetime"' | STRING ;

columnConstraint: '"primary"' | '"unique"' | '"required"' | '"auto_increment"' | '{' '"default"' ':' STRING '}' | '{' '"reference"' ':' STRING '}' | STRING ;
