from src.core import TableSelectionContext


class SelectionsInterpreter:
    def interpret(self, ctx: TableSelectionContext) -> tuple[str, list[str]]:
        # Extract table name
        table_name = ctx.tableName().IDENTIFIER().getText()

        # Extract selected columns
        columns = [col.IDENTIFIER().getText() for col in ctx.selectColumns().columnName()]

        return table_name, columns
    