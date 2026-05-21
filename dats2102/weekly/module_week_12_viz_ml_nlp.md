# Week 12 — Visualization for ML/NLP

> Visualizing machine learning and natural language processing outputs for interpretability and insight.

---

## 📖 Background & Motivation

Modern machine learning and NLP models generate complex outputs — from feature importances and prediction probabilities to topic clusters and embeddings. Visualization provides the bridge between model mechanics and human understanding. This week focuses on how to visualize model performance, interpret model decisions, and explore textual data patterns.

---

## 🔎 Learning Objectives

- Plot feature importance for classification and regression models.
- Visualize model performance with confusion matrices and ROC curves.
- Use embeddings and clustering visualizations to interpret NLP models.
- Generate word clouds and topic cluster plots using BERTopic.
- Understand visualization's role in the ML workflow for interpretability and trust.

---

## 📚 Readings & Resources

- *Hands-On Machine Learning with Scikit-Learn & TensorFlow* — chapters on model evaluation.
- scikit-learn: [Model Evaluation & Visualization](https://scikit-learn.org/stable/visualizations.html)
- BERTopic: [Topic Modeling & Visualization](https://maartengr.github.io/BERTopic/)
- WordCloud: [Python WordCloud Library](https://amueller.github.io/word_cloud/)
- [Interpretable ML Book by Christoph Molnar](https://christophm.github.io/interpretable-ml-book/)

**Sample Datasets:**

- IMDB Reviews (text sentiment classification)
- News Categories or 20 Newsgroups dataset
- Any scikit-learn classification dataset (e.g., iris, digits)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install scikit-learn matplotlib seaborn wordcloud bertopic numpy pandas  
pip install jupyter_compare_view datasets umap-learn hdbscan sentence-transformers
```

Confirm you can train a simple classifier, generate predictions, and render evaluation plots.

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Role of visualization in the ML workflow (10 min)
2. Model interpretability and explainability (10 min)
3. Feature importance and coefficient visualization (20 min)
4. Model evaluation plots: confusion matrix, ROC curve, precision-recall (20 min)
5. Discussion: visualization ethics and bias (15 min)

### Session 2 (75 min — Hands-on Focus)

1. Train and evaluate a classifier (IMDB reviews or scikit-learn dataset) (20 min)
2. Plot confusion matrix and ROC curve (20 min)
3. Visualize feature importances or SHAP-like explanations (15 min)
4. Generate word clouds and BERTopic clusters for NLP data (15 min)
5. Mini-workshop: interpret model predictions visually (5 min)
6. [Download the DBSCAN clustering example here](week12/DBSCAN.zip)
7. [Download the demo files for ML classification here](week12/week12.zip)
8. [Download the demo files NLP Topic Modeling here](week12/Week12_Visualization_for_ML_NLP2.ipynb)


---

## 💻 Starter Notebook Snippets

### Feature Importance Plot

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True, as_frame=True)
model = RandomForestClassifier(random_state=42).fit(X, y)
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values()

importances.plot(kind='barh', color='#4e79a7')
plt.title('Feature Importance — Random Forest')
plt.xlabel('Importance Score')
plt.show()
```

### Confusion Matrix and ROC Curve

```python
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, classification_report
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title('Confusion Matrix')
plt.show()

RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.title('ROC Curve')
plt.show()
```

### Word Cloud and Topic Clusters

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ' '.join(['great movie', 'terrible film', 'excellent acting', 'boring story'])
wc = WordCloud(width=600, height=300, background_color='white').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Example Word Cloud')
plt.show()
```

```python
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(subset='all')
docs = newsgroups.data[:200]

model = BERTopic(verbose=True)
topics, probs = model.fit_transform(docs)
model.visualize_topics()
```

---

## 🧪 In-Class Activity

- Plot feature importance and discuss which features drive predictions.
- Evaluate model performance visually using confusion matrix and ROC curve.
- Generate a word cloud summarizing frequent terms from text data.
- Use BERTopic to visualize clusters of topics from IMDB reviews or news data.
- Discuss visual explainability: how do these visualizations build model trust?

---

## 🏠 Homework

1. Choose either a structured dataset (classification/regression) **or** an NLP text dataset from Hugging Face (ag = load_dataset("ag_news")).
2. Produce:
      - One **feature importance** plot.
      - One **model evaluation visualization** (confusion matrix or ROC curve).
      - One **text visualization** (word cloud, BERTopic topic cluster, or BERTopic Topic Word Scores).
3. Include a 200–300 word reflection on how visualization supports model interpretability.
4. Submit `.ipynb` and `.html`.

---

## 🧩 Optional Extensions

- Create animated confusion matrices or topic evolution plots.
- Compare the performance of different classifiers.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.
