"""
views.py
this is where all routes are located
"""

from flask import Flask, jsonify, request
from flask_restful import Resource

orders = []

class Orders(Resource):
    # """post an order"""
    def post(self):
        order_data = {}
        data = request.get_json()
        order_data['food'] = data['food']
        order_data['quantity'] = data['quantity']
        order_data['food_id'] = len(orders)+1
        order_data['status'] = data['status']
        orders.append(order_data)
        return {'orders': order_data}, 201

    # """get a list of all orders"""
    def get(self):
        if len(orders) == 0:
            return {'message': 'No orders Available. Try to place an order using post'}, 404
        return {'orders': orders}, 200


class Order(Resource):
    # """get a specific order"""
    def get(self, order_id):
        order = [order for order in orders if order['food_id'] == order_id]
        if order:
            return {'order': order[0]},200
        else:
            return {'message': 'No specific order found'}, 404
          
    def put(self, order_id):
        order = [order for order in orders if order['food_id'] == order_id]
        if order:
            data = request.get_json()
            order[0]['food'] = data['food']
            order[0]['quantity'] = data['quantity']
            # order[0]['food_id'] = data['food_id']
            order[0]['status'] = data['status']
            return {'order': order[0]}, 200
        else:
            return {'message': 'Your order did not update'}, 404

    def delete(self, order_id):
        order = [order for order in orders if order['food_id'] == order_id]
        if order:
            del orders[0]
            return {'orders': orders}, 204
        else:
            return {'message': 'delete not successful'}, 404
