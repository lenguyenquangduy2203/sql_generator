from src.models.abstractions import SQNModel


class TypeSpec(SQNModel):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def to_sql(self) -> str:
        raise NotImplementedError("TypeSpec.to_sql() logic has not yet been implemented")

class ColumnDef(SQNModel):
    def __init__(self, column_name: str, type: TypeSpec) -> None:
        super().__init__()
        self.column_name = column_name
        self.type = type

    def to_sql(self) -> str:
        raise NotImplementedError("ColumnDef.to_sql() logic has not yet been implemented")

class DDLModel(SQNModel):
    def __init__(self, table_name: str, columns: list[ColumnDef]) -> None:
        super().__init__()
        self.table_name = table_name
        self.columns = columns

    def to_sql(self) -> str:
        # Remember to:
        # '*' -> table_name.lowercaseFirstLetter().concat('Id')
        # '@Table' -> 'Table.tableId'
        raise NotImplementedError("DDLModel.to_sql() logic has not yet been implemented")
    