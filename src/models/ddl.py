from src.models.abstractions import SQNModel


class TypeSpec(SQNModel):
    def __init__(self, name: str) -> None:
        self.name = name

    def to_sql(self) -> str:
        return self.name


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
        # Remember to:
        # '*' -> table_name.lowercaseFirstLetter().concat('Id')
        # '@Table' -> 'Table.tableId'
        if not self.columns:
            raise ValueError("CREATE TABLE must have at least one column.")

        columns_sql = ",\n  ".join(column.to_sql() for column in self.columns)
        return f"CREATE TABLE {self.table_name} (\n  {columns_sql}\n);"
