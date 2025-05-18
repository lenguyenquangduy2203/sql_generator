parser grammar DML;

import CommonParser;
options { tokenVocab = CommonLexer; }

dml: table_definition value_entries+;

// Take column name, table name are a must
table_definition: table_name LPAREN column_name (COMMA column_name)* RPAREN;

// Starts with '<<', followed by a parenthesized list of values
value_entries: SLF LPAREN value (COMMA value)* RPAREN;

table_name: IDENTIFIER;
column_name: IDENTIFIER;

// Can be strings, numbers (integer, float or long), or NULL
value: STRING | INT | FLOAT | LONG | NULL;

