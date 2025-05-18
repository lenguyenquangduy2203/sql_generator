grammar SQN;

import DDL, DML, Query, CommonParser;

options { tokenVocab = CommonLexer; }

program: statement+ EOF;
statement: ddl | dml | query;
