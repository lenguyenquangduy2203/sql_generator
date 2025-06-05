from src.models.abstractions import SQNModel

SQL_TYPE_MAP = {
    "int": "INTEGER",
    "str": "TEXT",
    "bool": "BOOLEAN",
    "float": "REAL",
    "date": "DATE",
    # Add or modify as needed
}

class TypeSpec(SQNModel):
    def __init__(self, name: str) -> None:
        self.name = name.lower()

    def to_sql(self) -> str:
        return SQL_TYPE_MAP.get(self.name, self.name.upper())


class ColumnDef(SQNModel):
    def __init__(self, column_name: str, type: TypeSpec) -> None:
        self.column_name = column_name
        self.type = type

    def to_sql(self) -> str:
        return f"{self.column_name} {self.type.to_sql()}"


class DDLModel(SQNModel):
    def __init__(self, table_name: str, columns: list[ColumnDef]) -> None:
        self.table_name = table_name
        self.columns = columns

    def to_sql(self) -> str:
        if not self.columns:
            raise ValueError("CREATE TABLE must have at least one column.")
        columns_sql = ",\n  ".join(col.to_sql() for col in self.columns)
        return f"CREATE TABLE {self.table_name} (\n  {columns_sql}\n);"
