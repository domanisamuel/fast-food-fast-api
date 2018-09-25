"""#unittest for test_views.py"""
import unittest

from app.api.v1.views import orders, order

class OrderTest(unittest.Testcase):
    def test_order(self): #tests if the route can get a specific order
    response = app.test_client().get('/api/v1/order/1')
    assert response.status_code == 200

    def test_order_fail(self):
    response = app.test_client().get('/api/v1/order/')
    assert response.status_code == 404

    def test_orders(self): #tests if the route can get list of oreders
    response = app.test_client().get('/api/v1/orders')
    assert response.status_code == 200

    def test_edit_order(self):
    response = app.test_client().put('/api/v1/order/', data = {'status': 1}, content_type = 'application/json')
    assert response.ststus_code == 404 #returns 404 if order is not found
