from enum import StrEnum, auto

class QueryType(StrEnum):
    CREATE = auto(),
    INSERT = auto(),
    SELECT = auto(),
    DROP = auto()