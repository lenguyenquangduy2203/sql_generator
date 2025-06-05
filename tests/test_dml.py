import unittest
from src.models.dml import TableDefinition, ValueEntry, DMLModel


class TestDMLModels(unittest.TestCase):
    def test_table_definition_to_sql(self):
        table_def = TableDefinition("Product", ["productID", "name", "price"])
        expected_sql = "INSERT INTO Product (productID, name, price) VALUES"
        self.assertEqual(table_def.to_sql(), expected_sql)

    def test_value_entry_to_sql(self):
        value_entry = ValueEntry([1, "Product 1", 50.0])
        expected_sql = "(1, 'Product 1', 50.0)"
        self.assertEqual(value_entry.to_sql(), expected_sql)

    def test_dml_model_to_sql(self):
        table_def = TableDefinition("Product", ["productID", "name", "price"])
        entries = [
            ValueEntry([1, "Product 1", 50.0]),
            ValueEntry([2, "Product 2", 75.5]),
        ]
        dml_model = DMLModel(table_def, entries)
        expected_sql = (
            "INSERT INTO Product (productID, name, price) VALUES\n"
            "(1, 'Product 1', 50.0),\n"
            "(2, 'Product 2', 75.5);"
        )
        self.assertEqual(dml_model.to_sql(), expected_sql)

    def test_dml_model_column_value_mismatch(self):
        table_def = TableDefinition("Product", ["productID", "name", "price"])
        entries = [
            ValueEntry([1, "Product 1"]),  # Missing price
        ]
        with self.assertRaises(ValueError) as context:
            DMLModel(table_def, entries).to_sql()
        self.assertEqual(str(context.exception), "number of columns and values DOES NOT match.")

    def test_dml_model_inconsistent_column_types(self):
        table_def = TableDefinition("Product", ["productID", "name", "price"])
        entries = [
            ValueEntry([1, "Product 1", 50.0]),
            ValueEntry([2, "Product 2", "75.5"]),  # Inconsistent type in price column
        ]
        with self.assertRaises(TypeError) as context:
            DMLModel(table_def, entries).to_sql()
        self.assertIn("Inconsistent data types in column 'price'", str(context.exception))


if __name__ == "__main__":
    unittest.main()