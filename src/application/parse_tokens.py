from antlr4 import CommonTokenStream, ParserRuleContext
from src.models.queries_factory.query_types import QueryType

def parse_tokens(tokens: CommonTokenStream, type: QueryType) -> ParserRuleContext:
    """
    Select the right ANTLR Parser by QueryType and parsing the token stream
    """
    pass
