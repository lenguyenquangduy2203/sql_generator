from antlr4 import CommonTokenStream, InputStream
from src.application.SqlInterpreter import SqlInterpreter
from src.core import CommonLexer, SQNParser


def generate_sql(sqn: str, interpreter: SqlInterpreter) -> str:
    input_stream = InputStream(sqn)
    lexer = CommonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SQNParser(token_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    models = interpreter.visit(tree)
    print(models)
    sql = ';\n'.join(model.to_sql() for model in models)
    return sql
