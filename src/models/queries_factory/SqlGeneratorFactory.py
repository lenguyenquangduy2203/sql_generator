from antlr4 import ParserRuleContext
from src.models.queries_factory import QueryType
from src.models.queries_factory.generators.SqlGenerator import SqlGenerator


def use_generator(sqn: str, type: QueryType) -> tuple[ParserRuleContext, SqlGenerator]:
    # TODO
    pass