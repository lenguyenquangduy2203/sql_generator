from src.models.abstractions import SQNModel
from typing import Any


class TableDefinition(SQNModel):
    def __init__(self, table_name: str, columns: list[str]) -> None:
        super().__init__()
        self.table_name = table_name
        self.columns = columns

    def to_sql(self) -> str:
        columns_sql = ", ".join(self.columns)
        return f"INSERT INTO {self.table_name} ({columns_sql}) VALUES "
        #raise NotImplementedError("TableDefinition.to_sql() logic has not yet been implemented")

class ValueEntry(SQNModel):
    def __init__(self, values: list[Any]) -> None:
        super().__init__()
        self.values = values

    def to_sql(self) -> str:
        print("Values:", self.values)  # Debugging output

        def parse_value(value):
            # Check if value is numeric
            if isinstance(value, str):
                try:
                    # Try converting to int
                    return int(value)
                except ValueError:
                    try:
                        # Try converting to float
                        return float(value)
                    except ValueError:
                        # If not numeric, return as string
                        return value
            return value

        # Extract and parse values
        extracted_values = [
            parse_value(v.getText() if hasattr(v, 'getText') else v)  # Use getText() for ANTLR contexts
            for v in self.values
        ]

        # Format values into SQL
        formatted_values = ", ".join(
            str(v) if isinstance(v, (int, float)) else f"'{v}'" if isinstance(v, str) else f"Unsupported({type(v).__name__})"
            for v in extracted_values
        )
        return f"({formatted_values})"
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
