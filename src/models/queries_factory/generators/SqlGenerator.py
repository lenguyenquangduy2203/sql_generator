from abc import ABC, abstractmethod
from antlr4 import ParserRuleContext


class SqlGenerator(ABC):
    """
    Abstract base class for SQL generators.

    Subclasses must implement the `generate` method to produce SQL queries.
    When implementing a subclass, ensure that the creation of the `ParserRuleContext`
    is encapsulated within the constructor (`__init__`). This allows the factory
    method to simply pass the query string to the generator, and the generator
    itself will handle the context creation.

    Example:
        class CreateTableGenerator(SqlGenerator):
            def __init__(self, query: str):
                `# Encapsulate context creation here`
                context = self._generate_context(query)
                super().__init__(context)

            def _generate_context(self, query: str) -> ParserRuleContext:
                `# Logic to create and return a ParserRuleContext`
                pass

            def generate(self) -> str:
                `# Logic to generate SQL`
                pass
    """

    def __init__(self, context: ParserRuleContext):
        super().__init__()
        self._ctx = context

    @abstractmethod
    def generate(self) -> str:
        pass
