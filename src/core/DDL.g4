parser grammar DDL;

import CommonParser;

options { tokenVocab = CommonLexer; }

ddl: tableName LPAREN columnDef (COMMA columnDef)* RPAREN;

tableName: IDENTIFIER;

columnDef: PK COLON typeSpec | FK IDENTIFIER COLON typeSpec | IDENTIFIER COLON typeSpec;
