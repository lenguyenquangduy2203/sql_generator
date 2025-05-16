grammar DML;

dml: statement+;
statement: insertSentence;

insertSentence: 'INSERT' 'INTO' table_name column_list? 'VALUES' value_list;

table_name: ID;
column_list: '(' column_name (',' column_name)* ')'; //Can accept multiple parenthesis such as: ('A', 'B'), ('C', 'D')
column_name: ID;
value_list: '(' value (',' value)* ')' | '(' value (',' value)* ',' value_list ')';
value: STRING | NUMBER | NULL;

//ID: [a-zA-Z_][a-zA-Z_0-9]*;
//STRING: '\'' (~'\'' | '\'\'' )* '\'';
//NUMBER: [0-9]+ ('.' [0-9]+)?;
//NULL: 'NULL';

//WS: [ \t\r\n]+ -> skip;