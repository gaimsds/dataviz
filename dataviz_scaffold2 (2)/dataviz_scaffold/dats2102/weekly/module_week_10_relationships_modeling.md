# Week 10 — Relationships & Modeling

> Visualizing relationships, correlations, and model fits to understand data patterns and predictive insights.

---

## 📖 Background & Motivation

Beyond distributions and comparisons, data visualization can help us understand **relationships** between variables and evaluate **model performance**. This week introduces how to visualize bivariate relationships, regression fits, residuals, and uncertainty, providing the foundation for interpreting linear and non‑linear trends.

Students will learn how to use scatterplots, trend lines, confidence intervals, and diagnostic plots to explore patterns and assess model fit, combining statistical modeling with visual storytelling.

---

## 🔎 Learning Objectives

- Create scatterplots to explore relationships between two or more variables.
- Visualize regression lines and confidence intervals.
- Understand correlation vs. causation and potential pitfalls.
- Evaluate model residuals visually to check fit and assumptions.
- Communicate model performance and uncertainty through effective visualization.

---

## 📚 Readings & Resources

- *Fundamentals of Data Visualization* — chapters on relationships & uncertainty.
- Seaborn: [regplot and lmplot](https://seaborn.pydata.org/tutorial/regression.html)
- Statsmodels: [OLS Regression](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html)
- [Visualizing Statistical Models](https://clauswilke.com/dataviz/statistical-models.html)

**Sample Data Sources:**

- Penguins dataset (bill length vs. flipper length)
- Housing price dataset (price vs. area)
- Gapminder (GDP vs. life expectancy)

---

## 🛠️ Setup Checklist

Ensure your environment includes:

```bash
pip install seaborn matplotlib statsmodels pandas numpy
```

Confirm you can run regression visualizations and calculate correlations using Seaborn and Statsmodels.

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Understanding relationships: correlation vs. causation (10 min)
2. Scatterplots and trend lines — visualizing associations (15 min)
3. Simple regression and confidence intervals (20 min)
4. Interpreting model fit and residuals visually (20 min)
5. Visual pitfalls: spurious correlation, overfitting, and omitted variables (10 min)
6. **Download** the [Jupyter Notebook](week10/Week10_relationships_modeling.ipynb)

### Session 2 (75 min — Hands-on Focus)

1. Creating scatterplots with regression fits in Seaborn (20 min)
2. Adding confidence intervals and customizing aesthetics (15 min)
3. Building an OLS regression model with Statsmodels (20 min)
4. Visualizing residuals and diagnostic plots (15 min)
5. Mini‑workshop: interpret one key relationship in your dataset (5 min)
6. **Download** the [Jupyter Notebook](week10/Week10_relationships_modeling_2.ipynb)
7. A **Working version of linked plotly plot** can be [downloaded here](week10/linked_plotly_plots.ipynb)

---

## 💻 Starter Notebook Snippets

### Scatterplot with regression fit

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna()
sns.lmplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", height=5, aspect=1.2)
plt.title("Flipper length vs Body mass with regression line")
plt.show()
```

### Correlation matrix heatmap

```python
import pandas as pd
corr = penguins.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation matrix of numeric features")
plt.show()
```

### Residual plot

```python
sns.residplot(data=penguins, x="flipper_length_mm", y="body_mass_g", lowess=True, color="#4e79a7")
plt.title("Residual plot: checking nonlinearity")
plt.show()
```

### Regression with Statsmodels

```python
import statsmodels.api as sm
X = penguins[["flipper_length_mm"]]
y = penguins["body_mass_g"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# Add predictions and visualize
penguins['pred'] = model.predict(X)
plt.scatter(penguins['flipper_length_mm'], y, label='Observed')
plt.plot(penguins['flipper_length_mm'], penguins['pred'], color='red', label='Fitted line')
plt.legend()
plt.title("OLS Regression Fit")
plt.show()
```

---

## 🧪 In-Class Activity

- Create scatterplots for multiple variable pairs and interpret patterns.
- Build a simple regression model and visualize fit and residuals.
- Discuss what model visualization reveals beyond summary statistics.
- Explore an example of spurious correlation and discuss implications.

---

## 🏠 Homework

1. Select a dataset of your choice (Try to avoid using integrated dataset).
2. Produce the following:
      - One **scatterplot** with regression fit and confidence interval.
      - One **correlation matrix heatmap**.
      - One **residual plot** illustrating model fit or deviation.
3. Include a brief interpretation (200–300 words) explaining:
      - What relationships you observed.
      - How visualization helped confirm or question your assumptions.
4. Submit `.ipynb` and `.html`.

**Rubric (10 pts)**

- Correct implementation of regression and correlation plots (4)
- Quality of interpretation and insights (3)
- Clarity of visualizations and labeling (2)
- Code reproducibility and documentation (1)

---

## 🧩 Optional Extensions

- Add multiple regression and visualize partial effects.
- Compare linear vs. non-linear fits.
- Visualize prediction intervals and uncertainty bands.
- Explore pairplots for multivariate relationships.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

- Use Quarto to render the notebook into HTML and zip the files for submission.

- Double-check the visualizations and your reflections in the HTML are properly organized and displayed.

