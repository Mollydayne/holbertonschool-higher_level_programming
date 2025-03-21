import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    try:
        products = []
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except FileNotFoundError:
        return []

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        product_list = read_json()
    elif source == "csv":
        product_list = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        product_list = [p for p in product_list if p["id"] == product_id]
        if not product_list:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=product_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
