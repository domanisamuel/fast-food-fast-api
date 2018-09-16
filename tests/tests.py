import unittest
from app import orders, app

class Testapp(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client

    def test_get_orders(self):
        response = self.client().get('http://localhost:5000/v1/orders')
        self.assertEqual(orders, response.data)

    def test_get_order_by_id(self):
        response = self.client().get('http://localhost:5000/v1/orders/4275')
        self.assertEqual(orders, response.data)

    def test_place_order(self):
        response = self.client().post('http://localhost:5000/v1/orders')
        self.assertEqual(orders, response.data)
        