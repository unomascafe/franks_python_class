# Lesson 29 — Building AI-Powered Tools

## What You'll Learn
- Combine AI APIs with your other Python skills
- Use structured outputs and tool use
- Build practical AI-powered automation

---

## Structured Outputs

Getting JSON back from Claude reliably:

```python
import anthropic
import json

client = anthropic.Anthropic()

def extract_structured(text, fields):
    """Ask Claude to extract specific fields as JSON."""
    field_list = ", ".join(fields)
    prompt = f"""Extract the following fields from this text as JSON: {field_list}
    
Text: {text}

Return ONLY valid JSON, no explanation."""
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response.content[0].text.strip()
    return json.loads(raw)


result = extract_structured(
    "Invoice #1042 from Acme Corp, dated March 15 2024, amount due: $450.00",
    ["invoice_number", "vendor", "date", "amount"]
)
print(result)
# {"invoice_number": "1042", "vendor": "Acme Corp", "date": "2024-03-15", "amount": 450.00}
```

---

## AI + File Processing

```python
import anthropic
from pathlib import Path

client = anthropic.Anthropic()

def summarize_file(filepath, max_tokens=500):
    """Read a file and summarize it with AI."""
    text = Path(filepath).read_text(encoding="utf-8")
    
    # Truncate if too long (simple approach)
    if len(text) > 50000:
        text = text[:50000] + "\n\n[... truncated ...]"
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=max_tokens,
        messages=[{
            "role": "user",
            "content": f"Summarize this document in bullet points:\n\n{text}"
        }]
    )
    return response.content[0].text


def classify_files(folder, categories):
    """Use AI to classify files by content."""
    results = {}
    for path in Path(folder).glob("*.txt"):
        content = path.read_text(encoding="utf-8")[:2000]
        prompt = f"""Classify this text into one of: {', '.join(categories)}
        
Text: {content}

Reply with ONLY the category name."""
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=20,
            messages=[{"role": "user", "content": prompt}]
        )
        results[path.name] = response.content[0].text.strip()
    return results
```

---

## AI + Web Scraping

```python
import requests
from bs4 import BeautifulSoup
import anthropic

client = anthropic.Anthropic()

def scrape_and_summarize(url):
    """Fetch a page and summarize its main content with AI."""
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Remove nav, footer, scripts
    for tag in soup(["nav", "footer", "script", "style"]):
        tag.decompose()
    
    text = soup.get_text(separator="\n", strip=True)[:10000]
    
    ai_response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": f"Summarize the key information from this webpage:\n\n{text}"
        }]
    )
    return ai_response.content[0].text
```

---

## AI + Flask: A Real AI Tool

```python
from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "text required"}), 400
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"Summarize in 3 bullet points:\n\n{data['text']}"
        }]
    )
    
    return jsonify({
        "summary": response.content[0].text,
        "tokens_used": response.usage.input_tokens + response.usage.output_tokens
    })
```

---

## Prompt Engineering Tips

These matter — a badly-written prompt gets bad results:

1. **Be specific about output format.** "Return JSON with keys: name, date, amount" beats "extract the info."
2. **Give examples (few-shot).** Show one input/output pair when the task is complex.
3. **System prompt for personality.** Use it to set role, tone, and constraints.
4. **Use `claude-haiku-4-5` for high-volume tasks.** It's fast and cheap for classification, extraction, and summarization.
5. **Handle failures.** AI can return unexpected formats — always wrap JSON parsing in try/except.

---

## Exercises

**Exercise 1:** Build an email classifier. Give it 10 sample emails (write them yourself) and have Claude classify each as: `"action_required"`, `"fyi"`, `"spam"`, or `"newsletter"`. Return results as a list of dicts.

**Exercise 2:** Build a Python code explainer: given a `.py` file path, read it and ask Claude to explain what it does in plain English — as if explaining to a non-programmer.

**Exercise 3:** Combine web scraping + AI: scrape 5 articles from a news site, summarize each one to 2 sentences, and save the results to a JSON file.

**Exercise 4 (stretch):** Build a "smart renamer" — given a folder of poorly-named files (like `doc1.txt`, `file_final_v3.txt`), read each one's first 500 characters and ask Claude to suggest a descriptive filename. Print the suggested renames and ask for confirmation before applying them.

---

## Key Takeaway
AI APIs are just functions that take text and return text. The power comes from combining them with everything else you know: file I/O, web scraping, databases, Flask. Keep prompts specific and output-format explicit. Use Haiku for volume, Sonnet/Opus for quality. Always handle parsing failures.

**Next:** [Lesson 30 — Intro to Machine Learning →](./30-ml-intro.md)
