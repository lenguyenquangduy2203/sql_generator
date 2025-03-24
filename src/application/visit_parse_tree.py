from antlr4 import ParserRuleContext
from src.models.queries_factory.query_types import QueryType

def visit_parse_tree(tree: ParserRuleContext, type: QueryType) -> str:
    """
    Select the right ANTLR Visitor by QueryType and generate SQL query
    """
    pass