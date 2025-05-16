parser grammar Query;

import Common;

options {tokenVocab = Common;}

query: selectQuery| updateQuery| deleteQuery;

selectQuery: 'SELECT' selectList   'FROM' tableName  whereClause?  groupByClause? orderByClause? limitClause?;

updateQuery: 'UPDATE' tableName'SET' assignment (',' assignment)* whereClause?;

deleteQuery: 'DELETE' 'FROM' tableName whereClause?;

selectList : '*' | columnName (',' columnName)*;

columnName: IDENTIFIER ('.' IDENTIFIER)?;

tableName: IDENTIFIER;

whereClause: 'WHERE' condition;

condition: predicate| condition 'AND' condition| condition 'OR' condition| '(' condition ')';

predicate: columnName operator value| columnName 'BETWEEN' value 'AND' value | columnName 'IN' '(' value (',' value)* ')'| columnName 'LIKE' STRING| columnName 'IS' 'NULL';

operator: '=' | '!=' | '<' | '>' | '<=' | '>=' ;

value: literal| columnName;

assignment: columnName '=' value;

groupByClause: 'GROUP' 'BY' columnName (',' columnName)*;

orderByClause: 'ORDER' 'BY' orderItem (',' orderItem)*;

orderItem: columnName ('ASC' | 'DESC')?;

limitClause: 'LIMIT' INT (',' INT)?;