grammar DML;

dml: table_definition value_entries+;

// Take column name, table name are a must
table_definition: table_name '(' column_name (',' column_name)* ')';

// Starts with '<<', followed by a parenthesized list of values
value_entries: '<<' '(' value (',' value)* ')';

table_name: ID;
column_name: ID;

// Can be strings, numbers, or NULL
value: STRING | NUMBER | NULL;

//ID: [a-zA-Z_][a-zA-Z_0-9]*;
//STRING: '\'' ( ~[\'] | '\'\'' )* '\'';
//NUMBER: [0-9]+ ('.' [0-9]+)?;
//NULL: 'NULL';

//WS: [ \t\r\n]+ -> skip;