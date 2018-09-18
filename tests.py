import unittest

from app import app, orders

from app import get_orders, get_order_by_id, place_order, update_order_status

class Testapp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    #test for get orders
    def test_get_orders(self):
        response = self.client().get('http://localhost:5000/v1/orders')
        self.assertEqual(orders, response.data)

    #test for get specific order
    def test_get_order_by_id(self):
        response = self.client().get('http://localhost:5000/v1/orders/4275')
        self.assertEqual(orders, response.data)
    #test for place order
    def test_place_order(self):
        response = self.client().post('http://localhost:5000/v1/orders')
        self.assertEqual(orders, response.data)

    