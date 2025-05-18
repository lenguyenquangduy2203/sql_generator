from src.core import TableSelectionContext


class SelectionsInterpreter:
    def interpret(self, ctx: TableSelectionContext) -> tuple[str, list[str]]:
        raise NotImplementedError("interpret() logic has not yet been implemented")