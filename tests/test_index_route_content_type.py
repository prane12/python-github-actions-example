import unittest
from app import app

class TestIndexRouteContentType(unittest.TestCase):
    def test_index_route_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()
