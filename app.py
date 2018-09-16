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
@app.route('/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

# Fetch a specific order
@app.route('/v1/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    required_order = []
    for order in orders:
        if order['order_id'] == order_id:
            required_order.append(order)
    if len(required_order) == 0:
        abort(404) 
    
    return jsonify({'order': required_order[0]})

# Place a new order.
@app.route('/v1/orders', methods=['POST'])
def place_order():
    if not request.json or not 'summary' in request.json:
        abort(404)
    
    order = [
        {
           "order_id": orders[-1]['order_id']+1,
            "customer_name": request.json['Name: '],
            "customer_phone":request.json['food: '],
            'acccepted': True
        }
    ]

    orders.append(order[0])
    return jsonify({'order': order}), 201

# Update the status of an order.
@app.route('/v1/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    required_order = []
    for order in orders:
        if order['order_id'] == order_id:
            required_order.append(order)
    if len(required_order) == 0:
        abort(404) 
    
    return jsonify({'order': required_order[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': not_found}), 404)

if __name__ == '__main__':
    app.run(debug=True)
