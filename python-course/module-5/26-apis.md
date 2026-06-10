# Lesson 26 — Building & Consuming APIs

## What You'll Learn
- Design a proper REST API with Flask
- Add authentication
- Consume third-party APIs in your own app
- Understand API design principles

---

## REST API Design

A REST API uses URLs as resources and HTTP methods as actions:

| Action | Method | URL |
|--------|--------|-----|
| List all items | GET | `/api/items` |
| Get one item | GET | `/api/items/42` |
| Create item | POST | `/api/items` |
| Update item | PUT/PATCH | `/api/items/42` |
| Delete item | DELETE | `/api/items/42` |

Use plural nouns for resources. Return appropriate status codes (200, 201, 400, 404, 500).

---

## A Complete CRUD API

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory "database"
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False, "created": "2024-01-10"},
]
next_id = 2


@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    done = request.args.get("done")
    if done is not None:
        filtered = [t for t in tasks if t["done"] == (done.lower() == "true")]
        return jsonify(filtered)
    return jsonify(tasks)


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    task = {
        "id": next_id,
        "title": data["title"],
        "done": False,
        "created": str(datetime.now().date()),
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = data["done"]
    return jsonify(task)


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return "", 204   # 204 No Content


if __name__ == "__main__":
    app.run(debug=True)
```

---

## Simple API Key Authentication

```python
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

VALID_API_KEYS = {"secret-key-123", "another-key-456"}


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key not in VALID_API_KEYS:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated


@app.route("/api/data")
@require_api_key
def protected_data():
    return jsonify({"data": "secret stuff"})
```

Test with:
```python
import requests
response = requests.get("http://localhost:5000/api/data",
                        headers={"X-API-Key": "secret-key-123"})
```

---

## Consuming an External API Inside Flask

Your Flask app can call other APIs:

```python
import requests as http_client
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/weather/<city>")
def weather_proxy(city):
    # Map city names to coordinates (simplified)
    coords = {
        "mesa": (33.4152, -111.8315),
        "phoenix": (33.4484, -112.0740),
    }
    if city.lower() not in coords:
        return jsonify({"error": "City not found"}), 404
    
    lat, lon = coords[city.lower()]
    response = http_client.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current_weather": True},
        timeout=10
    )
    return jsonify(response.json()["current_weather"])
```

---

## Exercises

Create `api_app.py`.

**Exercise 1:** Build the complete CRUD tasks API from above and test every endpoint using a separate `test_api.py` script that makes real `requests` calls.

**Exercise 2:** Add an `X-API-Key` header requirement to your API. Create two valid keys: one for read-only access (GET only) and one for full access.

**Exercise 3:** Add a `/api/tasks/stats` endpoint that returns a summary: total tasks, done count, pending count, and the oldest task.

**Exercise 4 (stretch):** Build a "proxy" Flask API that exposes a simplified weather endpoint. It calls Open-Meteo under the hood and returns a clean response: `{"city": "Mesa", "temp_f": 95.2, "condition": "sunny"}`. Handle the conversion from Celsius and the API's weather codes.

---

## Key Takeaway
REST APIs are just HTTP methods + URL resources. Use status codes correctly (200/201/400/404/500). CRUD is GET/POST/PATCH/DELETE. Protect endpoints with a decorator. Your Flask app can call other APIs — you can build pipelines of APIs.

**Next:** [Lesson 27 — Databases with SQLite →](./27-databases.md)
