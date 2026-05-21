# Week 4 — Wrangling with pandas

> Learning how to clean, transform, and prepare data for effective visualization.

---

## 📖 Background & Motivation

Data visualization is only as good as the data behind it. Most real-world datasets are messy, requiring cleaning and transformation before they can be meaningfully visualized. Pandas is the cornerstone Python library for data wrangling, providing flexible tools to reshape, aggregate, and join datasets. This week introduces practical techniques for preparing data that will allow you to build more accurate and insightful visualizations.

---

## 🔎 Learning Objectives

- Select, filter, group, summarize, and reshape data in pandas.
- Work with datetime and categorical data types.
- Join and merge datasets for richer analysis.
- Prepare clean datasets ready for visualization.

---

## 📚 Readings & Resources

- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Working with Text Data](https://pandas.pydata.org/docs/user_guide/text.html)
- [Time Series / Date Functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)

**Sample Data Sources:**

- NYC Taxi trips sample (NYC Open Data)
- COVID-19 data (Johns Hopkins University)

---

## 🛠️ Setup Checklist

Ensure you can run:

```bash
pip install pandas matplotlib seaborn
```

---

## 🧭 Lecture Outline

### Session 1 (75 min — Theory Focus)

1. Introduction to pandas DataFrames & Series
2. Selection and filtering operations
3. GroupBy and aggregation
4. Intro to joining and merging: **concepts and syntax**
5. Hands-on with NYC Taxi dataset. 
6. Download the files from [here](week4/file_list.md)



### Session 2 (75 min - Hands-On)

1. Recap & troubleshooting
2. Reshaping data: pivot, melt, stack/unstack
3. Working with datetime and categorical variables
4. Merging and joining multiple datasets
5. Download the [Jupyter Notebook](week4/week4_session2_hands_on_student.ipynb) and the [additional population table](week4/nyc_population_2024.csv) for the session.
6. Download the [complete Jupyter Notebook](week4/week4_session2_hands_on.ipynb). Remember to have other files ready for the notebook.


---

## 💻 Starter Notebook Snippets

```python
import pandas as pd

# Load dataset
trips = pd.read_csv("nyc_taxi_sample.csv")

# Filter rows
filtered = trips[trips["passenger_count"] > 2]

# Group and aggregate
agg = trips.groupby("passenger_count")["fare_amount"].mean()

# Reshape with melt
df_wide = pd.DataFrame({
    'id': [1, 2],
    'math': [90, 80],
    'english': [85, 78]
})
df_tidy = df_wide.melt(id_vars='id', var_name='subject', value_name='score')

# Parse dates
trips['pickup_datetime'] = pd.to_datetime(trips['pickup_datetime'])
```

---

## 🧪 In-Class Activity

- Use the COVID-19 dataset to:
  - Filter by one country and visualize new cases over time.
  - Group data by month and compare monthly averages.
  - Reshape the dataset to tidy form and create a plot.

---

## 🏠 Homework

1. Select a dataset with at least 5 columns.
2. Perform the following in a notebook:  
   a. Clean and filter the dataset.  
   b. Apply at least 2 groupby operations with aggregations.  
   c. Reshape the dataset at least once (pivot, melt, etc.).  
   d. Create 3 visualizations from the cleaned dataset.  
3. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Correct wrangling operations applied (4)
- Creativity in reshaping & grouping (2)
- Clear and readable plots (2)
- Reproducibility (2)

---

## 🧩 Optional Extensions

- Merge two datasets to add richer context.
- Explore pandas string operations to clean messy text.
- Create a time series plot with rolling averages.

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.

* The operations and visualizations in the Jupyter notebook are correct.
* Use Quarto to render the notebook and ensure the content is displayed well.
