from flask import Flask, jsonify, request

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

@app.route('/', methods=['GET'])
def returnAll():
    return jsonify({'orders': orders})

if __name__ == '__main__':
    app.run(debug=True)
