from src.application import parse_tokens, tokenize_input, visit_parse_tree
from src.models.queries_factory.query_types import QueryType

def build_sql_query(sqn: str, type: QueryType) -> str:
    tokens = tokenize_input(sqn, type);
    tree = parse_tokens(tokens, type);
    raw_sql_query = visit_parse_tree(tree, type);

    return raw_sql_query;
