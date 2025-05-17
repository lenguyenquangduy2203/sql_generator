grammar SQN;

import DDL, DML, Query, Common;

options { tokenVocab = Common; }

program: statement+ EOF;
statement: ddl | dml | query;
