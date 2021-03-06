# fast-food-fast-api

Fast-Food-Fast is an online food delievery app

- The API for the Fast Food Fast App that allows for fetching and chenging the status of an order

- It consist
`GET /api/v1/order/<int:order_id>` to fetch a single order
`GET /api/v1/orders` to fetch all orders
`PUT /api/v1/order/<int:order_id>` to change a specific order

| Endpoint | Functionality | 
|----------|---------------|
| GET /api/v1/order  | Get all the orders.|
| GET /api/v1/orders/ | Fetch a specific order |
| POST /api/v1/orders | Place a new order.|
| PUT /api/v1/orders/<orderId> | Update the status of an order.|

### Prerequisites
Python3 (A programming language)
Flask (A Python microframework)
Virtualenv (Stores all dependencies used in the project)
Pivotal Tracker (A project management tool)
Pytest (Tool for testing)
The app is hosted on heroku

### Getting Started:
Setting up the app locally.

Install pip:

`$ sudo apt-get install python-pip`

Clone this repository:

`$ git clone https://github.com/domanisamuel/fast-food-fast-api`

Get into the root directory:

`$ cd fast-food-fast/`

Install virtualenv:

`$ pip install virtualenv`

Create a virtual environment in the root directory:

`$ virtualenv -name of virtualenv-`

Note: If you do not have python3 installed globally, please run this command when creating a virtual environment:

`$ virtualenv -p python3 -name of virtualenv-`

Activate the virtualenv:

`$ source name of virtualenv/bin/activate`

Install the requirements of the project:

`$ pip install -r requirements.txt`

Create a file in the root directory called .env and add the two lines below

`export FLASK_APP="run.py"`

`export SECRET="some random string"`

Activate the env variables:

`$ source .env`

Run the application:

`$ python run.py`

To run tests:

`$ pytest`


[![Coverage Status](https://coveralls.io/repos/github/domanisamuel/fast-food-fast-api/badge.svg?branch=master)](https://coveralls.io/github/domanisamuel/fast-food-fast-api?branch=master)
