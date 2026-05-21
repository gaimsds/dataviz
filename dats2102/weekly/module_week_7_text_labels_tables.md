# Week 7 — Text, Labels, & Tables

> Enhancing clarity and storytelling through effective text, annotation, and tabular presentation.

---

## 📖 Background & Motivation

Numbers and charts alone rarely tell the full story. Effective use of **text, labels, annotations, and tables** can direct attention, clarify meaning, and strengthen the narrative of your visualization. This week focuses on best practices for integrating words with visuals, so your charts are not only accurate but also **understandable and memorable**.

We also cover how to design tables that are clear, accessible, and complementary to visualizations. In many professional contexts (reports, dashboards, publications), tables remain a key medium for communicating precise values alongside visuals.

---

## 🔎 Learning Objectives

- Add effective titles, axis labels, captions, and annotations to charts.
- Use direct labeling instead of or alongside legends.
- Highlight important data points with callouts and text placement.
- Design tables for clarity and readability, including alignment and formatting.
- Balance text and visuals to create compelling data stories.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — chapters on annotations and labeling.
- [Datawrapper Academy: How to annotate your charts](https://academy.datawrapper.de/article/118-how-to-annotate-your-charts)
- [Table Design Tips (Evergreen Data)](https://stephanieevergreen.com/designing-creative-tables/)
- Matplotlib: [text & annotation](https://matplotlib.org/stable/tutorials/text/annotations.html)
- Seaborn: [FacetGrid titles and labels](https://seaborn.pydata.org/tutorial/axis_grids.html)

**Sample Data Sources:**

- Sports statistics (e.g., player or team comparisons)
- Election results data
- Financial performance tables (company revenue, expenses, profits)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install pandas matplotlib seaborn
```

First, make sure the virtual environment is properly created and activated. Then confirm you can import these libraries and render a simple chart before class.

---

## 🧭 Lecture Outline

### Session 1 (Theory Focus + Hands-on)

1. Why text matters: the role of words in data storytelling
2. Titles, subtitles, and captions: framing interpretation
3. Legends vs. direct labeling: when to use each
4. Annotation techniques: highlighting key values or trends
5. Principles of clear table design
6. Adding labels and annotations in Matplotlib & Seaborn
7. Redesign a cluttered chart with better labeling
8. Create a table in pandas and format it for readability
9. Download the hands-on [Jupyter Notebook](week7/week7_hands_on.ipynb)
10. Download the extra [Jupyter Notebook for table formatting](week7/week7_hands_on_table_formatting.ipynb)


---

## 💻 Starter Notebook Snippets

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example scatterplot with annotation
penguins = sns.load_dataset("penguins").dropna()

sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Penguins: Flipper length vs Body mass")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")

# Annotate one point
max_penguin = penguins.loc[penguins['body_mass_g'].idxmax()]
plt.annotate("Heaviest penguin",
             xy=(max_penguin['flipper_length_mm'], max_penguin['body_mass_g']),
             xytext=(200, 6000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

```python
# Example formatted table in pandas
data = {
    'Team': ['A','B','C'],
    'Wins': [10, 12, 8],
    'Losses': [5, 3, 7]
}
df = pd.DataFrame(data)

# Pretty print with alignment
df.style.set_table_styles([
    {"selector": "th", "props": [("text-align", "center")]},
    {"selector": "td", "props": [("text-align", "center")]}
]).set_caption("Team Performance Summary")
```

---

## 🧪 In-Class Activity

- Take an unlabeled chart and add appropriate **title, labels, and annotations**.
- Recreate a sports statistics table and improve its formatting.
- Compare two versions of the same chart: one with only a legend, one with direct labeling.

---

## 🏠 Homework

1. Select a dataset (sports, election, or financial) and create:
    - One visualization with clear **title, labels, and at least two annotations**.
    - One **directly-labeled chart** (instead of legend-based).
    - One **formatted table** that complements your visualization.
2. Include a short reflection (200–300 words) explaining your labeling and table design choices.
3. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Effective use of titles, captions, and labels (3)
- Clear and purposeful annotations (2)
- Table design clarity and readability (3)
- Reflection quality (2)

---

## 🧩 Optional Extensions

- Experiment with `matplotlib.offsetbox` or custom text placement.
- Use color and font variations to emphasize annotations.
- Export a styled pandas DataFrame as an image or LaTeX table.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.
- The visualizations and your reflections in the Jupyter notebook are properly organized and displayed.
- Use Quarto to render the notebook into HTML and zip the files for submission.
