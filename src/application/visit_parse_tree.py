from antlr4 import ParserRuleContext
from src.models.queries_factory.query_types import QueryType

def visit_parse_tree(tree: ParserRuleContext, type: QueryType) -> dict:
    """
    Select the right ANTLR Visitor by QueryType and extract definition table into a dictionary
    """
    pass