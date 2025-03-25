from src.models.queries_factory.QueryType import QueryType
from src.models.queries_factory.QueryTypeIdentifier import identify_query_type
from src.models.queries_factory.SqlGeneratorFactory import use_generator


def build_sql_query(sqn: str) -> str:
    _type = identify_query_type(sqn)
    if (_type == QueryType.UNKNOWN):
        return ""
    
    ctx, generator = use_generator(sqn, _type)
    raw_sql_query = generator.generate(ctx)

    return raw_sql_query
