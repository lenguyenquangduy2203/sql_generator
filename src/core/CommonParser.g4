parser grammar CommonParser;

options { tokenVocab = CommonLexer; }

literal: INT | FLOAT | STRING | BOOLEAN | DATE | LONG | NULL ;

typeSpec: INT_TYPE | FLOAT_TYPE | STRING_TYPE | BOOLEAN_TYPE | LONG_TYPE | DATE_TYPE;
