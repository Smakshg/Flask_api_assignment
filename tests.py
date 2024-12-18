import unittest
from app import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_add_book(self):
        response = self.client.post("/books", json={
            "title": "Test Book",
            "author": "Test Author",
            "published_year": 2024
        })
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()