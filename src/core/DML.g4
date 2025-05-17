parser grammar DML;

import Common;
options {tokenVocab = Common;}

dml: table_definition value_entries+;

// Take column name, table name are a must
table_definition: table_name '(' column_name (',' column_name)* ')';

// Starts with '<<', followed by a parenthesized list of values
value_entries: '<<' '(' value (',' value)* ')';

table_name: IDENTIFIER;
column_name: IDENTIFIER;

// Can be strings, numbers (integer, float or long), or NULL
value: STRING | INT | FLOAT | LONG | NULL;

