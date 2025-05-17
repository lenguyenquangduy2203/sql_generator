parser grammar Query;

import Common;

options { tokenVocab = Common; }

query: tableSelection (';' tableSelection)* whereClause?;

tableSelection: tableName '~' selectColumns;

selectColumns: columnName (',' columnName)*;

whereClause: '?' condition;

condition: predicate| condition 'AND' condition| condition 'OR' condition| '(' condition ')';

predicate: columnName operator value| columnName 'BETWEEN' value 'AND' value| columnName 'IN' '(' value (',' value)* ')'| columnName 'LIKE' STRING| columnName 'IS' 'NULL';

operator: '=' | '!=' | '<' | '>' | '<=' | '>=';

value: literal | columnName;

columnName: IDENTIFIER ('.' IDENTIFIER)?;

tableName: IDENTIFIER;