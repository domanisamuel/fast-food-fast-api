from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

#data
orders = [
    {
        "order_id": 4232,
        "food": "Cheese Burger",
        "price": 400,
        "customer_name": "Shana Wambui",
        "customer_phone": 723456786
    },
    {
        "order_id": 5734,
        "food": "Chicken Burger",
        "price": 500,
        "customer_name": "Kelvin Kimani",
        "customer_phone": 723456786
    },
    {
        "order_id": 2235,
        "food": "Beef Burger",
        "price": 450,
        "customer_name": "Dorothy Wambua",
        "customer_phone": 723456786
    },
    {
        "order_id": 3452,
        "food": "Chilled Chicken Breast",
        "price": 570,
        "customer_name": "Kiki Wanja",
        "customer_phone": 723456786
    },
    {
        "order_id": 4275,
        "food": "Grilled Chicken Wing",
        "price": 350,
        "customer_name": "Allan Bett",
        "customer_phone": 723456786
    }
]

# Get all the orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

# Fetch a specific order
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    required_order = []
    for order in orders:
        if order['order_id'] == order_id:
            required_order.append(order)
    if len(required_order) == 0:
        abort(404) 
    
    return jsonify({'order': required_order[0]})

# Place a new order.

# Update the status of an order.

if __name__ == '__main__':
    app.run(debug=True)
