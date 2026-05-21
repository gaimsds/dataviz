# Week 6 — Comparisons

> Designing fair and effective comparisons across categories, groups, and time.

---

## 📖 Background & Motivation

Most insight in data science comes from **comparing** things: groups, treatments, time periods, geographies, and models. Good comparison graphics make differences and similarities **immediately legible** without misleading the audience. This week focuses on selecting the right comparison design (bars, dot plots, slope charts, small multiples), aligning scales and baselines, and avoiding visual pitfalls that distort comparisons.

---

## 🔎 Learning Objectives

- Choose appropriate designs for category and time comparisons (grouped bars, dot plots, slope charts, small multiples).
- Align scales, baselines, and axes to ensure fair comparisons.
- Normalize data (per capita, percent change, index to baseline) when appropriate.
- Use faceting and small multiples to reduce clutter and increase clarity.
- Add clear annotations and ordering to emphasize key contrasts.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — chapters on comparisons & small multiples.
- Seaborn: [Categorical plots](https://seaborn.pydata.org/tutorial/categorical.html), [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
- Matplotlib: [bar charts](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html), [subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
- ColorBrewer: [Choosing palettes](https://colorbrewer2.org/)

**Sample Data Sources:**

- World Bank indicators (e.g., GDP per capita, life expectancy)
- Gapminder (country-level indicators)
- Sports/team statistics (season-by-season comparisons)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install pandas numpy matplotlib seaborn plotly
```

First, ensure that the virtual environment is properly created and activated. Then confirm you can import these libraries and render a simple chart before class.

---

## 🧭 Lecture Outline

### Session 1 (Theory Focus)

1. When to compare? Framing questions and choosing the right comparison graphic
2. Bars vs. dot plots: perceptual accuracy and overplotting concerns
3. Slope charts for before/after and rank changes
4. Scale, baseline, and normalization (indexing to 100, percent change, per‑capita)
5. Small multiples and faceting; ordering and labeling for clarity
6. Download the Jupyter Notebook and data used in lecture from [this webpage](week6/file_list.md)

### Session 2 (Hands-on Focus)

1. Live coding: grouped bars → dot plot refactor
2. Build a slope chart for a before/after dataset
3. Create a small multiples view with `FacetGrid`
4. Mini‑workshop: add annotations, reorder categories, and test alternative scales
5. Download the [Jupyter Notebook](week6/Week06_HandsOn_Session2.ipynb) for this session.

---

## 💻 Starter Notebook Snippets

### Dot plot vs. grouped bars

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# toy data: mean score by group and condition
df = pd.DataFrame({
    "group": ["A","A","B","B","C","C"],
    "condition": ["Control","Treatment"]*3,
    "score": [72, 78, 65, 74, 81, 85]
})

# Grouped bars
sns.catplot(data=df, kind="bar", x="group", y="score", hue="condition")
plt.title("Grouped Bars")

# Dot plot (often clearer for two conditions)
sns.catplot(data=df, kind="point", x="group", y="score", hue="condition", dodge=True)
plt.title("Dot Plot Comparison")
```

### Slope chart (before/after)

```python
import numpy as np

before = pd.Series([72, 65, 81], index=["A","B","C"]).rename("before")
after = pd.Series([78, 74, 85], index=["A","B","C"]).rename("after")
long = pd.concat([before, after], axis=1).reset_index().melt(id_vars="index", var_name="time", value_name="score")
long = long.rename(columns={"index":"group"})

plt.figure(figsize=(6,4))
for g, sub in long.groupby("group"):
    xs = [0, 1]
    ys = sub.sort_values("time")["score"].values
    plt.plot(xs, ys, marker="o")
    plt.text(0-0.03, ys[0], g, ha="right", va="center")
plt.xticks([0,1],["Before","After"])
plt.title("Slope Chart — Before vs After")
plt.ylabel("Score")
plt.grid(axis='y', alpha=.3)
plt.tight_layout()
```

### Small multiples with FacetGrid

```python
# Using Gapminder-like structure
peng = sns.load_dataset("penguins").dropna()
fg = sns.FacetGrid(peng, col="species", height=3, sharey=True)
fg.map_dataframe(sns.scatterplot, x="flipper_length_mm", y="body_mass_g", alpha=.7)
fg.set_axis_labels("Flipper length (mm)", "Body mass (g)")
fg.set_titles(col_template="{col_name}")
```

### Normalization (indexing to a baseline)

```python
# Index each group to its first time value
wide = pd.DataFrame({"t":[1,2,3,4], "A":[100,110,108,120], "B":[100,98,105,112]})
base = wide.loc[0, ["A","B"]]
indexed = wide[["A","B"]].divide(base) * 100
indexed["t"] = wide["t"]
indexed_m = indexed.melt("t", var_name="series", value_name="index")
sns.lineplot(data=indexed_m, x="t", y="index", hue="series")
plt.axhline(100, color="k", lw=.8)
plt.ylabel("Index (baseline=100)")
plt.title("Indexed Comparison")
```

---

## 🧪 In-Class Activity

- Convert a cluttered grouped‑bar chart into a **dot plot** and explain which communicates differences more clearly.
- Build a **slope chart** for a before/after dataset and annotate the largest change.
- Create **small multiples** with `FacetGrid` to compare subgroups on the same scale.
- Try at least one **normalization** (percent change or index to baseline) and discuss how it changes the interpretation.

---

## 🏠 Homework

1. Select a dataset with at least two groups and either two conditions or multiple time points.
2. Produce the following:  
   a. One **dot plot** (or refactor from grouped bars) with thoughtful ordering and labels.  
   b. One **slope chart** showing before/after or the earliest vs. the latest comparison.  
   c. One **small‑multiples** chart (faceted) on a shared y‑scale.  
   d. At least one **normalized** view (percent change or index to baseline).  
3. Add concise annotations and a brief (100–200 words) discussion of which design best supports your comparison question and why.
4. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Appropriate chart choices for comparison tasks (3)
- Scale/baseline alignment and normalization where needed (3)
- Clear labeling, ordering, and annotations (2)
- Reproducibility and code quality (2)

---

## 🧩 Optional Extensions

- Use `plotly.express` to build an interactive small multiples or animation (e.g., by year).
- Explore **ranked dot plots** (ordered by value) and **slopegraphs** with many categories.
- Add **confidence intervals** or **error bars** for group comparisons.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.
- The visualizations and your reflections in the Jupyter notebook are properly organized and displayed.
- Use Quarto to render the notebook into HTML and zip the files for submission.
