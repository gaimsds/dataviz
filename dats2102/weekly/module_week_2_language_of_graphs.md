# Week 2 — Language of Graphs

> Understanding encodings, tidy data, and the grammar of graphics with Python. This module will deepen your ability to think critically about how information is mapped visually and how choices in data structure affect the clarity of your analysis.

---

## 📖 Background & Motivation

The "language" of data visualization comes from how we map variables to visual elements: position, shape, color, size, and scale. Mastering these encodings allows you to choose the right chart type and present information clearly. This week also introduces the concept of tidy data, a standard way of structuring datasets to facilitate easier analysis and visualization.

Beyond technical correctness, understanding these principles ensures that your work communicates insights effectively. Choosing the right encoding is about audience, purpose, and the kind of story you want your data to tell. For example, using color to differentiate categories can make a chart intuitive, but overusing it can lead to confusion. Similarly, reshaping data into tidy form streamlines your workflow and makes your notebooks reproducible and easier to understand for others. The combined skill set of visual encodings and tidy data practices represents the foundation for nearly every visualization you will create later in the course.

---

## 🔎 Learning Objectives

- Identify and apply core visual encodings (position, color, shape, size).
- Reshape datasets into tidy form for plotting.
- Create multi-encoding plots using seaborn and Altair’s grammar of graphics.
- Critically evaluate when and why to use specific encodings.

---

## 📚 Readings & Resources

- [The Grammar of Graphics (Wilkinson)](https://www.springer.com/gp/book/9780387245447) — conceptual foundation for how data maps to visuals.
- [Seaborn Categorical Plots](https://seaborn.pydata.org/tutorial/categorical.html) — useful introduction to encoding categorical variables.
- [Altair Tutorials](https://altair-viz.github.io/getting_started/) — practice with grammar of graphics in Python.
- [Tidy Data by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf) — essential reading for organizing datasets.
- [ggplot-style Visualization in Python (Real Python)](https://realpython.com/ggplot-python/) — practical tutorial for using ggplot concepts in Python.
- [ColorBrewer2](https://colorbrewer2.org/) — an interactive tool for choosing effective and accessible color schemes.

**Sample Data Sources for Practice:**

- [Seaborn Tips Dataset](https://seaborn.pydata.org/generated/seaborn.load_dataset.html) — classic dataset for learning encodings.
- [Gapminder Data via Plotly Express](https://plotly.com/python/gapminder-example/) — long-term country-level indicators.
- [Our World in Data](https://ourworldindata.org/) — a wide range of curated datasets.
- [Gapminder](https://www.gapminder.org/data/) — global development indicators with interactive visualization resources.

---

## 🛠️ Setup Checklist

Make sure your environment includes:

```bash
pip install pandas numpy matplotlib seaborn altair plotly
```

First make sure the virtual environment is properly created and activated. Then confirm you can import these libraries in a notebook and render a simple chart before class.

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Why tidy data matters in visualization workflows (10 min)
2. Core visual encodings: position, shape, color, size, and scale, with conceptual discussion and examples from research/literature (25 min)
3. Grammar of graphics overview: key ideas from Wilkinson and tidy data principles (20 min)
4. Class discussion: When encodings clarify vs. when they clutter (20 min)

### Session 2 (75 min — Hands-on Focus)

1. Seaborn’s approach to categorical vs. continuous data with live coding (20 min)
2. Altair grammar of graphics in Python with interactive demos (25 min)
3. Guided exercise: create multiple encodings in one chart, reflect on readability (20 min)
4. Workshop and Q&A: applying tidy reshaping and encodings to provided datasets (10 min)

---
### You can refer to the [Web page](week2/Week2_interactive_session.html) and download the [Jupyter Notebook](week2/Week2_interactive_session.ipynb)

---
## 💻 Notebook Snippets

### Load example dataset

```python
import seaborn as sns
import pandas as pd

# Load tips dataset
tips = sns.load_dataset("tips")
tips.head()
```

### Seaborn scatterplot with multiple encodings

```python
sns.scatterplot(
    data=tips,
    x="total_bill", y="tip",
    hue="day", style="time", size="size",
    palette="deep", sizes=(20, 200)
)
```

### Tidy data example

```python
# Pivot from wide to long (tidy)
df_wide = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'math': [90, 80],
    'english': [85, 78]
})

df_tidy = df_wide.melt(id_vars='name', var_name='subject', value_name='score')
```

### Altair example

```python
import altair as alt
alt.Chart(tips).mark_point().encode(
    x='total_bill',
    y='tip',
    color='day',
    shape='time',
    size='size'
)
```

---

## 🧪 In-Class Activity

- Using the `gapminder` dataset (via `plotly.express.data.gapminder()`), create:
  1. A scatterplot of GDP per capita vs. life expectancy.
  2. Encode continent as color and year as an animation frame.
- Discuss:&#x20;

  What does each encoding reveal?&#x20;

  Which encoding is most effective at showing inequality?&#x20;

  How does animation enhance or hinder interpretation?

**Hints**

```python
import plotly.express as px
gap = px.data.gapminder()
px.scatter(
    gap, x="gdpPercap", y="lifeExp",
    color="continent", size="pop",
    hover_name="country", animation_frame="year",
    log_x=True
)
```

---

## 🏠 Homework

1. Pick one dataset from the sample sources or bring your own.
2. Create **three different charts** using at least three distinct encodings.
3. For each chart, include:  
   a. A brief description of what the chart shows.  
   b. Why did you choose those encodings, and how did they help interpretation?  
   c. One limitation or challenge in readability.  
4. Submit `.ipynb` and `.html`  to Blackboard (You can zip the files together).

**Rubric (10 pts)**

- Correct application of tidy data principles (2)
- Effective and varied use of encodings (4)
- Chart clarity, proper labeling, and interpretability (2)
- Justification of choices and discussion of limitations (2)

---

## 🧩 Optional Extensions

- Use Altair to add interactive tooltips for deeper exploration.
- Compare the same visualization in Seaborn and Altair and note trade-offs.
- Explore `plotly.express` for creating interactive dashboards.
- Experiment with using **two vs. three encodings** in the same chart; evaluate which is clearer.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.

