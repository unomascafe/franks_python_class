# Lesson 28 — Working with AI APIs

## What You'll Learn
- Call the Anthropic (Claude) and OpenAI APIs from Python
- Handle streaming responses
- Manage tokens and costs
- Build reusable AI client wrappers

---

## Install

```bash
pip install anthropic openai
```

---

## Setup

Store your API keys in `.env` (never in code):

```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

```python
from dotenv import load_dotenv
import os
load_dotenv()
```

---

## Anthropic (Claude)

```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain Python decorators in 3 sentences."}
    ]
)

print(message.content[0].text)
```

### With a system prompt:

```python
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="You are a concise Python tutor. Keep examples short and practical.",
    messages=[
        {"role": "user", "content": "How do I sort a list of dicts by a key?"}
    ]
)
print(message.content[0].text)
```

### Multi-turn conversation:

```python
messages = []

def chat(user_message):
    messages.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=messages
    )
    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply

print(chat("What's the best way to handle errors in Python?"))
print(chat("Can you show me an example?"))   # remembers context
```

---

## OpenAI (GPT)

Very similar pattern:

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful Python tutor."},
        {"role": "user", "content": "What is a list comprehension?"}
    ]
)

print(response.choices[0].message.content)
```

---

## Streaming

For long responses, stream tokens as they're generated:

```python
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a Python function that..."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()  # newline at end
```

---

## Token Awareness

AI APIs charge per token (~¾ of a word). Monitor usage:

```python
response = client.messages.create(...)

print(f"Input tokens:  {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

Rough Claude pricing (check docs for current rates):
- `claude-haiku-4-5`: cheapest, fast
- `claude-sonnet-4-6`: balanced
- `claude-opus-4-8`: most capable, most expensive

Use Haiku for high-volume or simple tasks. Use Opus for complex reasoning.

---

## Exercises

Create `ai_basics.py`.

**Exercise 1:** Write a function `ask(question, model="claude-haiku-4-5")` that calls the Claude API and returns the response text. Test it with a few questions.

**Exercise 2:** Build a simple REPL (Read-Eval-Print Loop) chatbot that maintains conversation history. Type `quit` to exit.

**Exercise 3:** Write a function `summarize(text, max_words=100)` that uses Claude to summarize any text to a target length. Test it on a long article you copy-paste.

**Exercise 4:** Write a function `extract_data(text, schema_description)` that uses Claude to extract structured information from unstructured text and return it as a Python dict. For example: extract name, date, and amount from an email receipt.

**Exercise 5 (stretch):** Build a token-aware wrapper class that tracks total tokens used and estimated cost across multiple calls. Warn when you're approaching a budget limit.

---

## Key Takeaway
Both Anthropic and OpenAI use the same pattern: create a client, call `.create()` with a model name and a messages array, read `.content[0].text` or `.choices[0].message.content`. System prompts shape behavior. Multi-turn needs the full history in `messages`. Use streaming for long outputs. Track tokens — costs add up.

**Next:** [Lesson 29 — Building AI-Powered Tools →](./29-ai-tools.md)
