// SQLDML.g4
grammar SQLDML;

dmlStatement
    : selectStatement
    | insertStatement
    | updateStatement
    | deleteStatement
    ;

selectStatement
    : SELECT columnList FROM tableName (WHERE expression)?
    ;

insertStatement
    : INSERT INTO tableName '(' columnList ')' VALUES '(' valueList ')'
    ;

updateStatement
    : UPDATE tableName SET assignmentList (WHERE expression)?
    ;

deleteStatement
    : DELETE FROM tableName (WHERE expression)?
    ;

columnList
    : columnName (',' columnName)*
    ;

valueList
    : value (',' value)*
    ;

assignmentList
    : assignment (',' assignment)*
    ;

assignment
    : columnName '=' value
    ;

expression
    : orExpression
    ;

orExpression
    : andExpression ('OR' andExpression)*
    ;

andExpression
    : comparisonExpression ('AND' comparisonExpression)*
    ;

comparisonExpression
    : columnName comparisonOperator value
    ;

comparisonOperator
    : '='
    | '!='
    | '<'
    | '>'
    | '<='
    | '>='
    ;

value
    : STRING
    | NUMBER
    | NULL
    ;

columnName
    : IDENTIFIER
    ;

tableName
    : IDENTIFIER
    ;

NULL: 'NULL';

SELECT: 'SELECT';
INSERT: 'INSERT';
INTO: 'INTO';
VALUES: 'VALUES';
UPDATE: 'UPDATE';
SET: 'SET';
DELETE: 'DELETE';
FROM: 'FROM';
WHERE: 'WHERE';
AND: 'AND';
OR: 'OR';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '\'' (~['\r\n])* '\'';
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
