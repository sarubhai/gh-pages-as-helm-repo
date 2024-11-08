import json
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    { 'id': 1, 'name': 'Cakes' },
    { 'id': 2, 'name': 'Cookies' },
    { 'id': 3, 'name': 'Chocolates' },
    { 'id': 4, 'name': 'Milk' },
    { 'id': 5, 'name': 'Coffee' },
    { 'id': 6, 'name': 'Soft Drinks' },
    { 'id': 7, 'name': 'Ice cream' }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)


if __name__ == '__main__':
   app.run(debug=True)