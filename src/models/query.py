from src.models.abstractions import SQNModel, Condition, Value
from typing import Any

class PrimitiveType(Value):
    def to_sql(self) -> str:
        if isinstance(self.value, str):
            return f"'{self.value}'"
        elif self.value is None:
            return "NULL"
        elif isinstance(self.value, bool):
            return "TRUE" if self.value else "FALSE"
        return str(self.value)

class ColumnValue(Value):
    def to_sql(self) -> str:
        return self.column_name


class Predicate(Condition):
    def to_sql(self) -> str:
        return f"{self.column} {self.op} {self.value.to_sql()}"


class AndCondition(Condition):
    def to_sql(self) -> str:
        return f"{self.left.to_sql()} AND {self.right.to_sql()}"


class OrCondition(Condition):
    def to_sql(self) -> str:
        return f"{self.left.to_sql()} OR {self.right.to_sql()}"


class ParenCondition(Condition):
    def to_sql(self) -> str:
        return f"({self.inner.to_sql()})"


class QueryModel(SQNModel):
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
    def to_sql(self) -> str:
        return f"({self.query.to_sql()})"
