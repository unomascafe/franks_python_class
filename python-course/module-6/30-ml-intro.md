# Lesson 30 — Intro to Machine Learning

## What You'll Learn
- Understand the core ML concepts
- Train and evaluate a model with scikit-learn
- Know when to use ML vs AI APIs
- Where to go from here

---

## Install

```bash
pip install scikit-learn numpy pandas matplotlib
```

---

## ML vs AI APIs — When to Use Which

| Situation | Use |
|-----------|-----|
| You have labeled training data | ML (scikit-learn) |
| You need language understanding | AI API (Claude/GPT) |
| Real-time predictions on tabular data | ML |
| Open-ended generation or reasoning | AI API |
| You control the model | ML |
| You want zero training, fast deployment | AI API |

Most real projects use both.

---

## Core Concepts

**Supervised learning**: Learn from labeled examples → predict on new data.
- **Classification**: predict a category (spam/not spam, churn/retain)
- **Regression**: predict a number (price, sales, temperature)

**Unsupervised learning**: Find patterns in unlabeled data (clustering, anomaly detection).

**The workflow**:
1. Collect and clean data
2. Split into train/test sets
3. Train a model
4. Evaluate on the test set
5. Use the model to predict on new data

---

## A Complete Example: Classification

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Sample data: predict whether an employee will churn
data = pd.DataFrame({
    "years_at_company": [1, 5, 2, 8, 3, 7, 1, 4, 6, 2],
    "salary_band":       [1, 3, 2, 4, 2, 3, 1, 2, 3, 1],
    "satisfaction":      [2, 4, 3, 5, 2, 4, 1, 3, 5, 2],
    "churned":           [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
})

X = data[["years_at_company", "salary_band", "satisfaction"]]
y = data["churned"]

# Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

# Predict on new data
new_employee = pd.DataFrame([{
    "years_at_company": 1,
    "salary_band": 1,
    "satisfaction": 2,
}])
prediction = model.predict(new_employee)
probability = model.predict_proba(new_employee)
print(f"Churn prediction: {'Yes' if prediction[0] == 1 else 'No'}")
print(f"Churn probability: {probability[0][1]:.0%}")
```

---

## A Complete Example: Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

# Predict house price from size and bedrooms
np.random.seed(42)
n = 100
size = np.random.randint(800, 3000, n)
bedrooms = np.random.randint(1, 5, n)
price = size * 150 + bedrooms * 10000 + np.random.normal(0, 15000, n)

X = pd.DataFrame({"size": size, "bedrooms": bedrooms})
y = price

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"MAE: ${mean_absolute_error(y_test, y_pred):,.0f}")
print(f"R²: {r2_score(y_test, y_pred):.3f}")

# Predict
new_house = pd.DataFrame([{"size": 1500, "bedrooms": 3}])
print(f"Predicted price: ${model.predict(new_house)[0]:,.0f}")
```

---

## Feature Importance

Understand which inputs matter most:

```python
import matplotlib.pyplot as plt

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=True)

importance.plot(kind="barh")
plt.title("Feature Importance")
plt.tight_layout()
plt.show()
```

---

## Saving and Loading Models

```python
import joblib

# Save
joblib.dump(model, "churn_model.pkl")

# Load later
loaded_model = joblib.load("churn_model.pkl")
prediction = loaded_model.predict(new_data)
```

---

## Where to Go From Here

You now have the foundation. The next steps depend on your direction:

**More ML:**
- Deep learning: `tensorflow` / `pytorch`
- Natural language: `transformers` (Hugging Face)
- More algorithms: gradient boosting (`xgboost`, `lightgbm`)
- ML ops: `mlflow` for experiment tracking

**More AI/LLM work:**
- Tool use and agents (Claude / OpenAI function calling)
- RAG (Retrieval-Augmented Generation) with vector databases
- Fine-tuning models on your own data

**Good resources:**
- [scikit-learn docs](https://scikit-learn.org) — excellent tutorials
- [fast.ai](https://fast.ai) — practical deep learning
- [Kaggle](https://kaggle.com) — datasets and competitions for practice

---

## Exercises

**Exercise 1:** Use the Titanic dataset (search "Titanic CSV download" — it's classic and widely available). Build a classifier to predict survival. Try at least two different algorithms (`RandomForestClassifier` and `LogisticRegression`) and compare accuracy.

**Exercise 2:** Find a dataset that interests you (Kaggle has thousands). Do the full pipeline: load → clean → split → train → evaluate. Write comments explaining each step.

**Exercise 3:** Train a model and save it with `joblib`. Write a second script that loads the model and uses it to make predictions on new data you supply via the command line.

**Exercise 4 (stretch):** Combine ML + AI API: build a tool that uses scikit-learn to classify something (e.g., whether a support ticket needs escalation, based on word count and keywords), then uses Claude to draft an appropriate response based on the classification.

---

## Course Complete

You made it through all 30 lessons. Here's what you can now do:

- Write clean, idiomatic Python
- Work with files, data, and APIs
- Automate repetitive tasks
- Build CLI tools and web apps
- Work with databases
- Call AI APIs and build AI-powered tools
- Train and deploy basic ML models

The best way to keep improving: **build things**. Pick a problem you actually have, and solve it with Python. The gaps in your knowledge will make themselves obvious, and you'll know exactly what to learn next.

Good luck.
