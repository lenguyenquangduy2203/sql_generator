grammar JPAStyle;

import DDL, DML, Query, Common;

program: statement+ EOF;
statement: ddl | dml | query;
