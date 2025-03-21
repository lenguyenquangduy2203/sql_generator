import unittest
from app import app

class TestDashApp(unittest.TestCase):
    def test_app_title(self):
        self.assertEqual(app.title, "Dash")

if __name__ == "__main__":
    unittest.main()