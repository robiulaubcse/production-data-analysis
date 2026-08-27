# Production Data Analysis

## Project Overview

This project analyzes production data from a manufacturing environment to evaluate production performance, product quality, machine efficiency, shift performance, and downtime.

The project follows an end-to-end data analysis workflow, starting from data loading and cleaning through exploratory analysis, business insights, and dashboard development.

## Business Objectives

* Evaluate actual production against target production.
* Measure overall production achievement.
* Analyze product quality and rejection rates.
* Identify major causes of production downtime.
* Compare machine performance.
* Compare production performance across shifts.
* Compare performance across products.
* Present key findings through an interactive dashboard.

## Dataset

The dataset contains **367 production records** covering the period from **January to April 2026**.

Key fields include:

* Date
* Shift
* Production Line
* Machine
* Product
* Operator Count
* Target Quantity
* Actual Quantity
* Good Quantity
* Reject Quantity
* Downtime
* Cycle Time
* Defect Type
* Downtime Reason

> Note: The dataset is synthetic and is used for analytical and portfolio purposes.

## Analysis Workflow

### 1. Data Loading & Quality

Initial inspection of the dataset, including:

* Data types
* Missing values
* Duplicate records
* Basic statistical summaries
* Data quality checks

### 2. Data Cleaning

Data preparation included:

* Handling missing values
* Standardizing categorical values
* Cleaning product and defect categories
* Preparing the dataset for analysis

### 3. Exploratory Data Analysis

The analysis focused on:

* Production performance
* Achievement rate
* Quality performance
* Downtime
* Machine performance
* Shift performance
* Product performance
* Defect distribution
* Cycle time and efficiency

### 4. Business Insights

Key findings were summarized from the analysis to identify major operational patterns and potential improvement areas.

### 5. Dashboard

An interactive production performance dashboard was developed using **Streamlit** and **Plotly**.

Dashboard components include:

* Target vs Actual Production
* Achievement Rate
* Reject Rate
* Downtime
* Machine Performance
* Shift Performance

## Key Findings

* Overall production achievement was **101.52%**, meaning actual production slightly exceeded the planned target.
* Overall good production rate was **99.01%**.
* Overall reject rate was **0.99%**.
* **Material Shortage** and **Maintenance** were the two largest contributors to downtime, accounting for approximately **67.80%** combined.
* **M3** showed the highest machine-level production achievement.
* The **Night shift** achieved the highest production performance among the three shifts.
* **PRODUCT_C** showed the highest production achievement among the analyzed products.

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* Streamlit
* SQL
* Jupyter Notebook
* Git & GitHub

## Project Structure

```text
production-data-analysis/
│
├── data/
│   └── processed/
│       └── production_data_clean.csv
│
├── notebooks/
│   ├── 01_data_loading_and_quality.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   └── 04_business_insights.ipynb
│
├── src/
│   └── data_loading.py
│
├── dashboard/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/robiulaubcse/production-data-analysis.git
cd production-data-analysis
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run dashboard/app.py
```



Dashboard: https://appuction-data-analysis.streamlit.app/
