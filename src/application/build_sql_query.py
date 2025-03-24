from src.models.queries_factory.query_types import QueryType

def build_sql_query(extracted_data: dict, type: QueryType) -> str:
    """
    Select the right Builder by QueryType and convert extracted data into raw SQL query
    """
    pass
