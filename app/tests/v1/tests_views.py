"""#unittest for test_views.py"""
import unittest
import sys
import os


from app.api.v1.views import orders, order

class OrderTest(unittest.TestCase):
    #basic test for post
    def test_order(self): #tests if the route can get a specific folder
        order = self.client().post('/api/v1/order', data=self.order)
        self.assertEqual(order.status_code, 201)
        result = json.loads(order.data.decode('utf-8'))
        self.assertEqual(result['food'], 'chicken burger')
    #basic test for get all orders
    def test_orders(self):
        response = self.client().get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)

    #basic test to get one / specific order
    def test_order(self):
        response = self.client().get('/api/v1/order/1')
        self.assertEqual(response.status_code, 200)

    #basic test to delete an order
    def test_order(self):
        response = self.client().delete('/api/v1/order/1')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()