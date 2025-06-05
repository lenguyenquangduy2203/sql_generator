from src.models.abstractions import SQNModel, Condition, Value
from typing import Any

class PrimitiveType(Value):
    def __init__(self, value: Any):
        super().__init__(value)

    def to_sql(self) -> str:
        if isinstance(self.value, str):
            return f"'{self.value}'"
        elif self.value is None:
            return "NULL"
        elif isinstance(self.value, bool):
            return "TRUE" if self.value else "FALSE"
        return str(self.value)


class ColumnValue(Value):
    def __init__(self, column_name: str):
        self.column_name = column_name

    def to_sql(self) -> str:
        return self.column_name


class Predicate(Condition):
    def __init__(self, column: str, op: str, value: Value):
        self.column = column
        self.op = op
        self.value = value

    def to_sql(self) -> str:
        return f"{self.column} {self.op} {self.value.to_sql()}"


class AndCondition(Condition):
    def __init__(self, left: Condition, right: Condition):
        self.left = left
        self.right = right

    def to_sql(self) -> str:
        return f"{self.left.to_sql()} AND {self.right.to_sql()}"


class OrCondition(Condition):
    def __init__(self, left: Condition, right: Condition):
        self.left = left
        self.right = right

    def to_sql(self) -> str:
        return f"{self.left.to_sql()} OR {self.right.to_sql()}"


class ParenCondition(Condition):
    def __init__(self, inner: Condition):
        self.inner = inner

    def to_sql(self) -> str:
        return f"({self.inner.to_sql()})"


class QueryModel(SQNModel):
    def __init__(
        self,
        selections: Optional[Dict[str, List[str]]] = None,
        conditions: Optional[Condition] = None,
    ):
        super().__init__(selections, conditions)

    def to_sql(self) -> str:
        select_clauses = []
        for table, columns in self.selections.items():
            for column in columns:
                select_clauses.append(f"{table}.{column}")
        select_sql = ", ".join(select_clauses) or "*"

        from_tables = ", ".join(self.selections.keys())
        where_clause = f" WHERE {self.conditions.to_sql()}" if self.conditions else ""

        return f"SELECT {select_sql} FROM {from_tables}{where_clause}"


class SubqueryValue(Value):
    def __init__(self, query: QueryModel):
        self.query = query

    def to_sql(self) -> str:
        return f"({self.query.to_sql()})"

