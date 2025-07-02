# 🧹 Data Quality Checker

## Overview
This project is a visual utility that helps data scientists and analysts quickly inspect common data issues such as missing values, duplicate rows, invalid negative entries, and statistical outliers. Designed to accelerate the data cleaning phase before modeling or analysis.

## 🛠️ Features
- Missing value detection and heatmap
- Duplicate row finder
- Negative value checker for numerical columns
- Z-score-based outlier detection
- Interactive charts using Plotly (boxplots, scatter plots)
- Summarized quality report in terminal

## 🧪 Simulated Dataset
The dataset is generated with:
- Intentional missing values
- Intentional duplicates
- Negative values where not expected
- Outliers in numerical fields

## 📦 Technologies Used
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Plotly

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install pandas numpy seaborn matplotlib plotly
```

### 2. Run the Script
```bash
python data_quality_checker.py
```

The script will use:
- A synthetic broken dataset (`simulated_hr_dataset.csv`)
- Multiple plots and summaries highlighting issues in the dataset

## 📊 Sample Outputs
- Terminal summary of missing, duplicate, and outlier entries
- Visual plots: Heatmap for missing data, Boxplot for outliers, and scatter plots for anomalies

## 🔍 Key Takeaways
- Visual profiling is an efficient way to catch data issues early.
- Rule-based detection is highly customizable and interpretable.
- Great foundation for building more advanced profiling or data quality tools.

## 💡 Future Enhancements
- Export detailed quality report as PDF/HTML
- Add more advanced anomaly detection models (e.g., Isolation Forest)
- Embed into a Streamlit app for real-time dataset uploads
