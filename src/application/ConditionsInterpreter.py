from src.application.SqlInterpreter import SqlInterpreter
from src.core import ConditionContext
from src.models.query import Predicate


class ConditionsInterpreter:
    def __init__(self, interpreter: SqlInterpreter) -> None:
        self.interpreter = interpreter

    def interpret(self, ctx: ConditionContext) -> Predicate:
        raise NotImplementedError("interpret() logic has not yet been implemented")