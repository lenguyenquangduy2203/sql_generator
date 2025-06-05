from src.core import ConditionContext
from src.core.SQNVisitor import SQNVisitor
from src.models.query import Predicate


class ConditionsInterpreter:
    def interpret(self, ctx: ConditionContext, interpreter: SQNVisitor) -> Predicate:
        raise NotImplementedError("interpret() logic has not yet been implemented")