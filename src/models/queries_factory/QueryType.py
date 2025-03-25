from enum import StrEnum, auto


class QueryType(StrEnum):
    UNKNOWN = auto(),
    CREATE = auto(),
    INSERT = auto(),
    SELECT = auto(),
    DROP = auto()