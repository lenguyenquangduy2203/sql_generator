parser grammar DDL;

import Common;

ddl: tableName '(' columnDef (',' columnDef)* ')';

tableName: IDENTIFIER;

columnDef: PK ':' typeSpec | FK ':' typeSpec | STRING ':' typeSpec;

PK: '*';

FK: '@' STRING;
