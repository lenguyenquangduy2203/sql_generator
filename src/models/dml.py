from src.models.abstractions import SQNModel
from typing import Any


class TableDefinition(SQNModel):
    def __init__(self, table_name: str, columns: list[str]) -> None:
        super().__init__()
        self.table_name = table_name
        self.columns = columns

    def to_sql(self) -> str:
        raise NotImplementedError("TableDefinition.to_sql() logic has not yet been implemented")

class ValueEntry(SQNModel):
    def __init__(self, values: list[Any]) -> None:
        super().__init__()
        self.values = values

    def to_sql(self) -> str:
        raise NotImplementedError("ValueEntry.to_sql() logic has not yet been implemented")

class DMLModel(SQNModel):
    def __init__(self, definition: TableDefinition, entries: list[ValueEntry]) -> None:
        super().__init__()
        self.definition = definition
        self.entries = entries

    def to_sql(self) -> str:
        # Remember to:
        # Check value entries types so that all columns have the same type
        raise NotImplementedError("DMLModel.to_sql() logic has not yet been implemented")
