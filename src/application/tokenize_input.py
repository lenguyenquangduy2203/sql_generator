from antlr4 import CommonTokenStream
from src.models.queries_factory.query_types import QueryType

def tokenize_input(sqn: str, type: QueryType) -> CommonTokenStream:
    """
    Select the right ANTLR Lexer by QueryType and tokenizing the input
    """
    pass