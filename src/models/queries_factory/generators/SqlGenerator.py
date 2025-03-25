from abc import ABC, abstractmethod
from antlr4 import ParserRuleContext


class SqlGenerator(ABC):
    @abstractmethod
    def generate(ctx: ParserRuleContext) -> str:
        pass