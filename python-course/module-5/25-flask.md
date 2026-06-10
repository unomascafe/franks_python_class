# Lesson 25 — Simple Web Apps with Flask

## What You'll Learn
- Build a basic web server with Flask
- Handle routes and URL parameters
- Return HTML and JSON
- Use templates

---

## Install

```bash
pip install flask
```

---

## Hello World

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)
```

```bash
python app.py
# Visit http://localhost:5000
```

`debug=True` auto-reloads when you save the file — essential during development.

---

## Routes and URL Parameters

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Home page"

@app.route("/about")
def about():
    return "About page"

# URL parameter
@app.route("/user/<username>")
def profile(username):
    return f"Profile: {username}"

# Typed parameter
@app.route("/item/<int:item_id>")
def item(item_id):
    return f"Item #{item_id}"
```

---

## Returning JSON (API Endpoints)

```python
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Nozzle Kit", "price": 15.50},
    {"id": 2, "name": "Filament", "price": 22.99},
]

@app.route("/api/products")
def get_products():
    return jsonify(products)

@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(product)
```

---

## Query Parameters

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    limit = request.args.get("limit", 10, type=int)
    return f"Searching for '{query}', limit {limit}"
```

```
GET /search?q=filament&limit=5
```

---

## Handling POST Requests

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400
    
    # In a real app, save to database here
    new_user = {"id": 99, "name": data["name"]}
    return jsonify(new_user), 201   # 201 = Created
```

---

## HTML Templates

Flask uses Jinja2 templates. Create a `templates/` folder:

```
app.py
templates/
  index.html
  product.html
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head><title>Products</title></head>
<body>
  <h1>Products</h1>
  <ul>
    {% for product in products %}
    <li>{{ product.name }} — ${{ product.price }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    products = [
        {"name": "Nozzle Kit", "price": 15.50},
        {"name": "Filament", "price": 22.99},
    ]
    return render_template("index.html", products=products)
```

---

## Exercises

Create `app.py` with a `templates/` folder alongside it.

**Exercise 1:** Build a Flask app with three routes: `/` (home), `/about`, and `/contact`. Each returns a basic HTML page.

**Exercise 2:** Build a mini product API with in-memory data (a list of dicts). Implement:
- `GET /api/products` — all products
- `GET /api/products/<id>` — single product (404 if not found)
- `POST /api/products` — add a product (from JSON body)

Test it with a browser and a short script using `requests`.

**Exercise 3:** Build a simple dashboard page that shows a list of 3D printing projects from an in-memory list. Use a template with a for loop.

**Exercise 4 (stretch):** Add a search endpoint: `GET /api/products?q=nozzle` that filters products by name (case-insensitive). Return only matching products.

---

## Key Takeaway
Flask turns Python functions into web routes with `@app.route()`. `jsonify()` returns JSON. `request.args` gets query params, `request.get_json()` gets a POST body. Templates go in `templates/`. `debug=True` during development only — never in production.

**Next:** [Lesson 26 — Building & Consuming APIs →](./26-apis.md)
