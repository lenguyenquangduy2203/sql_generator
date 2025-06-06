import unittest
from src.models.ddl import TypeSpec, ColumnDef, DDLModel


class TestDDLModels(unittest.TestCase):
    def test_type_spec_to_sql(self):
        type_spec = TypeSpec("int")
        self.assertEqual(type_spec.to_sql(), "INTEGER")

        type_spec = TypeSpec("string")
        self.assertEqual(type_spec.to_sql(), "TEXT")

    def test_column_def_to_sql(self):
        type_spec = TypeSpec("int")
        column_def = ColumnDef("productId", type_spec)
        self.assertEqual(column_def.to_sql(), "productId INTEGER")

        type_spec = TypeSpec("string")
        column_def = ColumnDef("productName", type_spec)
        self.assertEqual(column_def.to_sql(), "productName TEXT")

    def test_ddl_model_to_sql(self):
        columns = [
            ColumnDef("productId", TypeSpec("int")),
            ColumnDef("productName", TypeSpec("string")),
            ColumnDef("price", TypeSpec("float")),
        ]
        ddl_model = DDLModel("Product", columns)
        expected_sql = (
            "CREATE TABLE Product (\n"
            "  productId INTEGER,\n"
            "  productName TEXT,\n"
            "  price FLOAT\n"
            ");"
        )
        self.assertEqual(ddl_model.to_sql(), expected_sql)

    def test_ddl_model_empty_columns(self):
        ddl_model = DDLModel("EmptyTable", [])
        with self.assertRaises(ValueError) as context:
            ddl_model.to_sql()
        self.assertEqual(str(context.exception), "CREATE TABLE must have at least one column.")


if __name__ == "__main__":
    unittest.main()