import unittest
from src.models.query import (
    PrimitiveType,
    ColumnValue,
    Predicate,
    AndCondition,
    OrCondition,
    ParenCondition,
    QueryModel,
    SubqueryValue,
)


class TestQueryModels(unittest.TestCase):
    def test_primitive_type_to_sql(self):
        self.assertEqual(PrimitiveType("string").to_sql(), "'string'")
        self.assertEqual(PrimitiveType(None).to_sql(), "NULL")
        self.assertEqual(PrimitiveType(True).to_sql(), "TRUE")
        self.assertEqual(PrimitiveType(False).to_sql(), "FALSE")
        self.assertEqual(PrimitiveType(123).to_sql(), "123")
        self.assertEqual(PrimitiveType(45.67).to_sql(), "45.67")

    def test_column_value_to_sql(self):
        column_value = ColumnValue("column_name")
        self.assertEqual(column_value.to_sql(), "column_name")

    def test_predicate_to_sql(self):
        predicate = Predicate("column_name", "=", PrimitiveType("value"))
        self.assertEqual(predicate.to_sql(), "column_name = 'value'")

        predicate = Predicate("column_name", ">", PrimitiveType(123))
        self.assertEqual(predicate.to_sql(), "column_name > 123")

    def test_and_condition_to_sql(self):
        left = Predicate("column1", "=", PrimitiveType("value1"))
        right = Predicate("column2", ">", PrimitiveType(100))
        and_condition = AndCondition(left, right)
        self.assertEqual(
            and_condition.to_sql(),
            "column1 = 'value1' AND column2 > 100"
        )

    def test_or_condition_to_sql(self):
        left = Predicate("column1", "=", PrimitiveType("value1"))
        right = Predicate("column2", "<", PrimitiveType(50))
        or_condition = OrCondition(left, right)
        self.assertEqual(
            or_condition.to_sql(),
            "column1 = 'value1' OR column2 < 50"
        )

    def test_paren_condition_to_sql(self):
        inner = Predicate("column1", "=", PrimitiveType("value1"))
        paren_condition = ParenCondition(inner)
        self.assertEqual(paren_condition.to_sql(), "(column1 = 'value1')")

    def test_query_model_to_sql(self):
        selections = {
            "table1": ["column1", "column2"],
            "table2": ["column3"]
        }
        conditions = AndCondition(
            Predicate("table1.column1", "=", PrimitiveType("value1")),
            Predicate("table2.column3", ">", PrimitiveType(100))
        )
        query_model = QueryModel(selections, conditions)
        expected_sql = (
            "SELECT table1.column1, table1.column2, table2.column3 "
            "FROM table1, table2 "
            "WHERE table1.column1 = 'value1' AND table2.column3 > 100"
        )
        self.assertEqual(query_model.to_sql(), expected_sql)

    def test_subquery_value_to_sql(self):
        selections = {"table1": ["column1"]}
        conditions = Predicate("table1.column1", "=", PrimitiveType("value1"))
        subquery = QueryModel(selections, conditions)
        subquery_value = SubqueryValue(subquery)
        expected_sql = (
            "(SELECT table1.column1 FROM table1 WHERE table1.column1 = 'value1')"
        )
        self.assertEqual(subquery_value.to_sql(), expected_sql)


if __name__ == "__main__":
    unittest.main()