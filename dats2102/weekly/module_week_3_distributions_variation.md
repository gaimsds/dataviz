# Week 3 — Distributions & Variation

> Exploring distributions, variation, and choices in single-variable visualization.

---

## 📖 Background & Motivation

Understanding how data is distributed is the foundation of exploratory data analysis. Whether we want to know if flight delays cluster around certain times or if iris flower species differ in petal length, distribution plots reveal the shape, spread, and potential outliers. Poorly chosen or misinterpreted plots can obscure variation and mislead conclusions.

Distributions are more than just “shapes of data”. They tell us about **central tendency** (where the bulk of data lies), **spread** (how much variation exists), **skewness** (whether data is lopsided), and **outliers** (values that are unusual or extreme). These insights form the basis for both descriptive statistics and inferential modeling. For data scientists, knowing how to visualize distributions effectively is an essential skill for diagnosing problems, preparing data, and communicating results.

---

## 🔎 Learning Objectives

- Choose and interpret appropriate distribution plots.
- Apply binning strategies and kernel density estimation.
- Construct and read empirical cumulative distribution functions (ECDFs).
- Compare plots to understand spread, skewness, and outliers.
- Critically evaluate the strengths and weaknesses of each distribution visualization technique.

---

## 📚 Readings & Resources

- [Seaborn Distribution Plots](https://seaborn.pydata.org/tutorial/distributions.html) — practical guide to histograms, KDEs, and more.
- [Matplotlib Histograms](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html) — documentation for histogram basics.
- [EDA Concepts](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15) — blog overview of exploratory data analysis.
- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/histograms-density-plots.html) — chapter on histograms and density plots.

**Sample Data Sources:**

- Flight delay data (US DOT Bureau of Transportation Statistics)
- Iris dataset (`seaborn.load_dataset('iris')`)
- Titanic dataset (Kaggle / Seaborn)
- COVID-19 case data (Our World in Data)

---

## 🛠️ Setup Checklist

Ensure you can run:

```bash
pip install seaborn matplotlib pandas
```

Check that you can load the iris dataset and render a histogram before class.

---

## 🧭 Lecture Outline

### Session 1 (75 min)

1. Motivation: Why study distributions? Examples from real-world datasets (10 min)
2. Histograms & binning choices: impact of bin width on interpretation (20 min)
3. Kernel density estimation: intuition, bandwidth selection, pros/cons (25 min)
4. Hands-on with iris dataset: plot histograms and KDEs for sepal/petal features (20 min)

### Session 2 (75 min)

1. Recap & troubleshooting from Session 1 (10 min)
2. Boxplots & violin plots: comparing categories and visualizing spread (25 min)
3. ECDF: cumulative view of distributions, why it’s useful (20 min)
4. Workshop: students choose dataset, produce 2–3 distribution plots, peer feedback (20 min)

---
### You can refer to the [Jupyter Notebook template](week3/week3_hands_on_template.ipynb)

---

## 💻 Starter Notebook Snippets

```python
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

# Histogram
sns.histplot(iris['sepal_length'], bins=20, kde=False)

# KDE
sns.kdeplot(iris['sepal_length'], fill=True)

# Boxplot by species
sns.boxplot(data=iris, x='species', y='sepal_length')

# ECDF
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(x)+1) / len(x)
    return x, y

import numpy as np
x, y = ecdf(iris['sepal_length'])
plt.plot(x, y, marker='.', linestyle='none')
plt.xlabel('Sepal length')
plt.ylabel('ECDF')
```

---

## 🧪 In-Class Activity

- Compare histogram vs. KDE of flight delay data. Which communicates central tendency more clearly? Which better shows multimodality?
- Plot boxplot of iris petal length by species. Discuss: how does this compare to histograms?
- Construct ECDFs for sepal width. What does it reveal about spread and skewness?
- Group work: each team selects a dataset and produces multiple distribution plots, then explains which is most effective.

---

## 🏠 Homework

1. Select **one dataset** (one from the Sample Data Sources or one of your choice).
2. For the dataset:  
   a. Produce at least 3 distribution plots (histogram, KDE, ECDF, box/violin).  
   b. Interpret shape, spread, skew, and outliers in markdown.  
   c. Reflect on the pros/cons of each visualization type.  
   d. Add at least one annotated chart highlighting a key pattern.  
3. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Correct use of multiple plot types (4)
- Clear interpretation and discussion (3)
- Labeling, annotations, and readability (2)
- Reproducibility (1)

---

## 🧩 Optional Extensions

- Experiment with different bin sizes in histograms and compare results.
- Overlay histogram and KDE to show complementarity.
- Use `sns.pairplot` to examine multiple distributions and correlations.
- Compare distributions across groups using facet plots.
- Try violin plots with split by category.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.
