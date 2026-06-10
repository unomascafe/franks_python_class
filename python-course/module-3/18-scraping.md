# Lesson 18 — Web Scraping

## What You'll Learn
- Scrape HTML pages with `requests` + `BeautifulSoup`
- Find and extract elements by tag, class, and attribute
- Handle pagination
- Know when scraping is appropriate

---

## Install

```bash
pip install requests beautifulsoup4
```

---

## How It Works

1. Fetch the HTML with `requests`
2. Parse it with `BeautifulSoup`
3. Find the elements you want
4. Extract the data

```python
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
```

---

## Finding Elements

```python
# Find the first matching element
soup.find("h1")
soup.find("div", class_="product-name")
soup.find("a", href=True)

# Find all matching elements (returns a list)
soup.find_all("li")
soup.find_all("a", class_="btn")
soup.find_all("p", limit=5)

# CSS selectors (often cleaner)
soup.select("div.product > h2")
soup.select_one("nav ul li.active")
```

---

## Extracting Data

```python
element = soup.find("h1")

element.text          # text content (with whitespace)
element.get_text(strip=True)   # text, stripped of extra whitespace

element["href"]       # get an attribute value
element.get("href")   # safe version — returns None if missing

# Example: get all links
for a_tag in soup.find_all("a"):
    href = a_tag.get("href")
    text = a_tag.get_text(strip=True)
    if href:
        print(f"{text}: {href}")
```

---

## A Real Example

Scrape book titles and prices from `books.toscrape.com` (a practice scraping site):

```python
import requests
from bs4 import BeautifulSoup

def scrape_books(url="https://books.toscrape.com"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = []
    for article in soup.select("article.product_pod"):
        title = article.find("h3").find("a")["title"]
        price = article.select_one("p.price_color").get_text(strip=True)
        rating = article.find("p", class_="star-rating")["class"][1]
        books.append({"title": title, "price": price, "rating": rating})
    
    return books

books = scrape_books()
for book in books[:5]:
    print(f"{book['title']} — {book['price']} ({book['rating']} stars)")
```

---

## Handling Pagination

```python
import requests
from bs4 import BeautifulSoup

def scrape_all_pages(base_url):
    all_books = []
    page = 1
    
    while True:
        url = f"{base_url}/catalogue/page-{page}.html"
        response = requests.get(url)
        
        if response.status_code == 404:
            break   # no more pages
        
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod h3 a")
        
        for book in books:
            all_books.append(book["title"])
        
        page += 1
    
    return all_books
```

---

## Be a Good Citizen

Before scraping a site:
- Check `/robots.txt` — it specifies what's allowed
- Don't hammer servers — add `time.sleep(1)` between requests
- Use the site's API if one exists — it's always better
- Don't scrape personal data without a clear, legitimate reason

---

## Exercises

Create `scraping.py`. Use `https://books.toscrape.com` — it's a practice site built for scraping.

**Exercise 1:** Scrape the first page and print all 20 book titles, prices, and star ratings.

**Exercise 2:** Scrape all pages and find the 10 cheapest books across the entire site.

**Exercise 3:** Scrape books by category — find the "Mystery" category, scrape all books in it, and save them to a CSV file.

**Exercise 4 (stretch):** Add error handling and retries to your scraper. If a request fails, wait 2 seconds and try again up to 3 times before giving up.

---

## Key Takeaway
`requests` fetches the HTML, `BeautifulSoup` parses it. `.find()` gets one element, `.find_all()` gets all matches, `.select()` uses CSS selectors. Always use `.get_text(strip=True)` for text and `.get("attr")` for attributes. Respect `robots.txt` and add delays between requests.

**Next:** [Lesson 19 — Automation Scripts →](./19-automation.md)
