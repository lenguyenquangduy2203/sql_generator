from src.models.abstractions import SQNModel, Condition, Value
from typing import Any


class PrimitiveType(Value):
    def __init__(self, value: Any) -> None:
        # value is typed for the time being
        # could change to the supported types during implementation
        super().__init__()
        self.value = value

    def to_sql(self) -> str:
        raise NotImplementedError("PrimitiveType.to_sql() logic has not yet been implemented")

class ColumnValue(Value):
    def __init__(self, column_name: str) -> None:
        super().__init__()
        self.column_name = column_name

    def to_sql(self) -> str:
        raise NotImplementedError("ColumnValue.to_sql() logic has not yet been implemented")
    
class Predicate(Condition):
    def __init__(self, column: str, op: str, value: Value) -> None:
        super().__init__()
        self.column = column
        self.op = op
        self.value = value

    def to_sql(self) -> str:
        raise NotImplementedError("Predicate.to_sql() logic has not yet been implemented")
    
class AndCondition(Condition):
    def __init__(self, left: Condition, right: Condition) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def to_sql(self) -> str:
        raise NotImplementedError("AndCondition.to_sql() logic has not yet been implemented")
    
class OrCondition(Condition):
    def __init__(self, left: Condition, right: Condition) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def to_sql(self) -> str:
        raise NotImplementedError("OrCondition.to_sql() logic has not yet been implemented")
    
class ParenCondition(Condition):
    def __init__(self, inner: Condition) -> None:
        super().__init__()
        self.inner = inner

    def to_sql(self) -> str:
        raise NotImplementedError("ParenCondition.to_sql() logic has not yet been implemented")
    
class QueryModel(SQNModel):
    def __init__(self, selections: dict[str, list[str]], conditions: Condition) -> None:
        super().__init__()
        self.selections = selections
        self.conditions = conditions

    def to_sql(self) -> str:
        raise NotImplementedError("QueryModel.to_sql() logic has not yet been implemented")
    
class SubqueryValue(Value):
    def __init__(self, query: QueryModel) -> None:
        super().__init__()
        self.query = query

    def to_sql(self) -> str:
        raise NotImplementedError("SubqueryValue.to_sql() logic has not yet been implemented")