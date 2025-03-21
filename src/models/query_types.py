from enum import StrEnum, auto

class QueryType(StrEnum):
    CREATE_TABLE = auto(),
    CREATE_DATABASE = auto(),
    INSERT = auto(),
    SELECT = auto(),
    DROP_TABLE = auto(),
    DROP_DATABASE = auto()