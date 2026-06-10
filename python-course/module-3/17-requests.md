# Lesson 17 — HTTP Requests & APIs

## What You'll Learn
- Make GET and POST requests with `requests`
- Work with JSON API responses
- Handle auth, headers, and errors
- Understand REST APIs

---

## Install

```bash
pip install requests
```

---

## GET Requests

Fetch data from a URL:

```python
import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)   # 200
print(response.json())         # parsed JSON as a dict
print(response.text)           # raw response as string
```

**Always check the status code.** `200` = OK. `404` = not found. `401` = unauthorized. `500` = server error.

```python
response = requests.get("https://api.example.com/data")

if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

Or use `raise_for_status()` to auto-raise on errors:

```python
response = requests.get("https://api.example.com/data")
response.raise_for_status()   # raises HTTPError if status >= 400
data = response.json()
```

---

## Query Parameters

Pass parameters in the URL cleanly:

```python
# Instead of: "https://api.example.com/search?q=python&limit=10"
params = {"q": "python", "limit": 10}
response = requests.get("https://api.example.com/search", params=params)
```

---

## Headers & Auth

```python
# API key in header
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get("https://api.example.com/data", headers=headers)

# Basic auth
response = requests.get("https://api.example.com/", auth=("username", "password"))
```

---

## POST Requests

Send data to an API:

```python
import requests

# Send JSON
payload = {"name": "Frank", "email": "frank@example.com"}
response = requests.post("https://api.example.com/users", json=payload)

# Send form data
response = requests.post("https://api.example.com/login",
                         data={"username": "frank", "password": "secret"})
```

---

## A Real Example: Public APIs

```python
import requests

# Open-Meteo: free weather API, no key needed
def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["current_weather"]

weather = get_weather(33.4152, -111.8315)  # Mesa, AZ
print(f"Temp: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h")
```

---

## Error Handling

```python
import requests

def safe_get(url, **kwargs):
    try:
        response = requests.get(url, timeout=10, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection failed")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    return None
```

---

## REST API Concepts

Most APIs you'll work with are REST APIs. They use standard HTTP methods:

| Method | Use |
|--------|-----|
| `GET` | Read data |
| `POST` | Create data |
| `PUT` / `PATCH` | Update data |
| `DELETE` | Delete data |

Resources are addressed by URL: `/users/42`, `/products/`, `/orders/7/items/`.

---

## Exercises

Create `requests_demo.py`.

**Exercise 1:** Make a GET request to `https://httpbin.org/get` and print the response. Then make a request to `https://httpbin.org/get?name=Frank&city=Mesa` using the `params` argument and print the `args` field from the response.

**Exercise 2:** Use the [Open-Meteo API](https://open-meteo.com/en/docs) to get the current temperature in Mesa, AZ. Print it in both Celsius and Fahrenheit.

**Exercise 3:** Use the GitHub API (no auth needed for public data) to get info about a public repo:
```
https://api.github.com/repos/python/cpython
```
Print the repo name, description, star count, and open issue count.

**Exercise 4:** Write a `RateLimitedRequester` class (or a simple function with a delay) that waits 1 second between requests. Use `time.sleep(1)`. Test it by making 3 requests in a row.

**Exercise 5 (stretch):** Use the [JSONPlaceholder API](https://jsonplaceholder.typicode.com) to:
- GET all posts (`/posts`)
- Filter to posts by user ID 1
- POST a new fake post and print the response
- Print a summary of the results

---

## Key Takeaway
`requests.get(url)` → `.json()` is the core pattern. Always handle errors — use `raise_for_status()` or check `status_code`. Pass params as a dict, not a hand-built URL string. JSON responses come back as Python dicts/lists — work with them normally.

**Next:** [Lesson 18 — Web Scraping →](./18-scraping.md)
