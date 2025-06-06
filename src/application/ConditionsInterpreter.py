from src.core import ConditionContext
from src.core.SQNVisitor import SQNVisitor
from src.models.abstractions import Condition
from src.models.query import (
    Predicate,
    AndCondition,
    OrCondition,
    ParenCondition,
    PrimitiveType,
    ColumnValue,
    SubqueryValue,
    QueryModel,
)


class ConditionsInterpreter:
    def interpret(self, ctx: ConditionContext, interpreter: SQNVisitor) -> Condition:
        # Handle predicate
        if ctx.predicate():
            return self.visit_predicate(ctx.predicate(), interpreter)

        # Handle AND condition
        elif ctx.AND():
            left = self.interpret(ctx.condition(0), interpreter)
            right = self.interpret(ctx.condition(1), interpreter)
            return AndCondition(left, right)

        # Handle OR condition
        elif ctx.OR():
            left = self.interpret(ctx.condition(0), interpreter)
            right = self.interpret(ctx.condition(1), interpreter)
            return OrCondition(left, right)

        # Handle parenthesized condition
        elif ctx.LPAREN():
            inner = self.interpret(ctx.condition(0), interpreter)
            return ParenCondition(inner)

        raise ValueError("Unsupported condition type")

    def visit_predicate(self, ctx, interpreter: SQNVisitor) -> Condition:
        # Handle columnName operator value
        if ctx.operator():
            column = ctx.columnName().IDENTIFIER().getText()
            op = ctx.operator().getText()
            value_ctx = ctx.value()
            value = self.visit_value(value_ctx, interpreter)
            return Predicate(column, op, value)

        # Handle columnName BETWEEN value AND value
        elif ctx.BETWEEN():
            column = ctx.columnName().IDENTIFIER().getText()
            value1 = self.visit_value(ctx.value(0), interpreter)
            value2 = self.visit_value(ctx.value(1), interpreter)
            return Predicate(column, "BETWEEN", PrimitiveType(f"{value1.to_sql()} AND {value2.to_sql()}"))

        # Handle columnName IN (value, value, ...)
        elif ctx.IN():
            column = ctx.columnName().IDENTIFIER().getText()
            values = [self.visit_value(v, interpreter) for v in ctx.value()]
            values_sql = ", ".join(v.to_sql() for v in values)
            return Predicate(column, "IN", PrimitiveType(f"({values_sql})"))

        # Handle columnName LIKE STRING
        elif ctx.LIKE():
            column = ctx.columnName().IDENTIFIER().getText()
            string_value = ctx.STRING().getText()
            return Predicate(column, "LIKE", string_value)

        # Handle columnName IS NULL
        elif ctx.IS():
            column = ctx.columnName().IDENTIFIER().getText()
            return Predicate(column, "IS", PrimitiveType("NULL"))

        raise ValueError("Unsupported predicate type")

    def visit_value(self, ctx, interpreter: SQNVisitor):
        # Cannot extract condition value
        # Error: 'list' object has no attribute 'literal'
        # Handle literal values
        if ctx.literal():
            return PrimitiveType(interpreter.visitLiteral(ctx.literal()))

        # Handle columnName values
        elif ctx.columnName():
            return ColumnValue(ctx.columnName().IDENTIFIER().getText())

        # Handle subquery values
        elif ctx.query():
            subquery = interpreter.visitQuery(ctx.query())
            return SubqueryValue(subquery)

        raise ValueError("Unsupported value type")