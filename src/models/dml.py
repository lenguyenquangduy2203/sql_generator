from src.models.abstractions import SQNModel
from typing import Any


class TableDefinition(SQNModel):
    def __init__(self, table_name: str, columns: list[str]) -> None:
        super().__init__()
        self.table_name = table_name
        self.columns = columns

    def to_sql(self) -> str:
        columns_sql = ", ".join(self.columns)
        return f"INSERT INTO {self.table_name} ({columns_sql})"
        #raise NotImplementedError("TableDefinition.to_sql() logic has not yet been implemented")

class ValueEntry(SQNModel):
    def __init__(self, values: list[Any]) -> None:
        super().__init__()
        self.values = values

    def to_sql(self) -> str:
        formatted_values = ", ".join(f"'{v}'" if isinstance(v, str) else str(v) for v in self.values)
        return f"VALUES ({formatted_values})"
        #raise NotImplementedError("ValueEntry.to_sql() logic has not yet been implemented")

class DMLModel(SQNModel):
    def __init__(self, definition: TableDefinition, entries: list[ValueEntry]) -> None:
        super().__init__()
        self.definition = definition
        self.entries = entries

    def to_sql(self) -> str:
        if not self.entries:
            raise ValueError("At least 1 entry must be provided for INSERT.")

        num_columns = len(self.definition.columns)

        for entry in self.entries:
            if len(entry.values) != num_columns:
                raise ValueError("number of columns and values DOES NOT match.")

        for col_idx in range(num_columns):
            column_types = {type(entry.values[col_idx]) for entry in self.entries}
            if len(column_types) > 1:
                raise TypeError(f"Inconsistent data types in column '{self.definition.columns[col_idx]}'.")

        header = self.definition.to_sql()
        values_sql = ",\n".join(entry.to_sql() for entry in self.entries)
        return f"{header}\n{values_sql};"
	#raise NotImplementedError("ValueEntry.to_sql() logic has not yet been implemented")
