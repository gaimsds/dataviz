# Week 5 — Perception & Principles

> Applying visual perception theory and design principles to create effective, truthful, and clear visualizations.

---

## 📖 Background & Motivation

Even when the data is clean and the chart type is appropriate, design decisions can make the difference between clarity and confusion. Human perception imposes limits on how well we can decode visual information. By understanding principles from perceptual psychology, we can design graphics that communicate more effectively and avoid misleading audiences.

This week introduces concepts like Cleveland & McGill’s hierarchy of graphical perception, preattentive attributes, Gestalt principles, and common pitfalls in chart design. These theoretical foundations provide guidance for making practical design decisions in your visualizations.

---

## 🔎 Learning Objectives

- Understand how human perception shapes data interpretation.
- Apply the Cleveland–McGill perceptual rankings to select more effective encodings.
- Identify and use preattentive features to guide viewer attention.
- Recognize and correct misleading design practices.

---

## 📚 Readings & Resources

- [Cleveland & McGill (1984): Graphical Perception](https://www.jstor.org/stable/2288400)
- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/) — Chapters on perception and design.
- [Data Visualization Society: Design Principles](https://medium.com/nightingale)
- [The Gestalt Principles](https://www.interaction-design.org/literature/topics/gestalt-principles?srsltid=AfmBOoqEP2imze0vgkjwq9VBrODWkOAzKIDhm9G7euqQKJtlb_8NWcUw)

**Sample Data Sources:**

- Simulated datasets designed to illustrate perception issues.
- Any dataset from previous weeks (for redesign exercises).

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install seaborn matplotlib pandas
```

---

## 🧭 Lecture Outline

### Session 1 (Theory Focus)

1. Motivation: Why perception matters in visualization 
2. Cleveland–McGill hierarchy of graphical perception
3. Preattentive attributes (color, shape, position, orientation)
4. Gestalt principles and visual grouping
5. Misleading charts and design pitfalls

### Session 2 (Hands-on Focus)

1. Recap & discussion of theory
2. Redesign bad charts into effective versions
3. Guided exercise: compare encodings using simulated data
4. Workshop: students bring prior homework plots and improve them
5. Download the [Jupyter Notebook](week5/Week5_Session2_HandsOn_class.ipynb) 
---

## 💻 Starter Notebook Snippets

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example of a misleading bar chart
values = [5, 10, 15]
labels = ['A', 'B', 'C']

plt.bar(labels, values)
plt.ylim(4, 16)  # Misleading y-axis range
plt.title("Misleading Bar Chart")
plt.show()

# Redesigned chart with zero baseline
plt.bar(labels, values)
plt.ylim(0, 16)
plt.title("Improved Bar Chart")
plt.show()
```

---

## 🧪 In-Class Activity

- Critique provided "poorly-designed" charts and redesign them.
- Use preattentive attributes to highlight important data points.
- Compare multiple encoding strategies for the same dataset.

---

## 🏠 Homework

1. Find a poorly designed chart (for example, a truncated y-axis bar chart from a news article, a rainbow-colored heatmap in a research paper, or an infographic with distorted area encodings).
2. Recreate the chart faithfully in Python.  
3. Redesign the chart applying perception & design principles.  
4. Write a short reflection (200+ words) describing:  
   a. Why the original was misleading or ineffective.  
   b. What principles guided your redesign?  
   c. How your redesign improves comprehension.  
5. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Accurate reproduction of the original chart (2)
- Effective redesign applying principles (4)
- Clear reflection linking to theory (2)
- Visual clarity and labeling (2)

---

## 🧩 Optional Extensions

- Experiment with alternative encodings and compare effectiveness.
- Conduct a quick peer survey: which design is easier to interpret?
- Try adding annotations or highlights using preattentive cues.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.
- The visualizations and your reflections in the Jupyter notebook are properly organized and displayed.
- Use Quarto to render the notebook into HTML and zip the files for submission.

