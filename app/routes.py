from flask import Flask, request, jsonify, render_template
import json

def load_data():
    try:
        with open('data/stock_data.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"error": str(e)}

def home():
    return render_template('home.html')

def get_stocks():
    exchange_code = request.json.get('exchange')
    data = load_data()
    
    if "error" in data:
        return jsonify(data)
    
    for exchange in data:
        if exchange["code"] == exchange_code:
            return jsonify(exchange["topStocks"])
    return jsonify([])

def get_price():
    exchange_code = request.json.get('exchange')
    stock_code = request.json.get('stock')
    data = load_data()
    
    if "error" in data:
        return jsonify(data)
    
    for exchange in data:
        if exchange["code"] == exchange_code:
            for stock in exchange["topStocks"]:
                if stock["code"] == stock_code:
                    return jsonify({"price": stock["price"]})
    return jsonify({"price": None})

def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/stocks', 'get_stocks', get_stocks, methods=['POST'])
    app.add_url_rule('/price', 'get_price', get_price, methods=['POST'])
