# __init__.py file
# packaging the app

from flask import Flask

from flask_restful import Api

app = Flask(__name__)
api_endpoint = Api(app)

from app.api.v1.views import Orders, Order

api_endpoint.add_resource(Orders, '/v1/orders')
api_endpoint.add_resource(Order, '/v1/order/<int:order_id>')
