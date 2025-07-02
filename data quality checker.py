import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv("simulated_hr_dataset.csv")

# ------------------------------
# BASIC STRUCTURE
# ------------------------------
print("🔍 Dataset Preview:")
print(df.head(), "\n")

print("🧮 Dataset Info:")
print(df.info(), "\n")

print("📏 Shape:", df.shape)
print("-" * 50)

# ------------------------------
# 1. MISSING VALUE CHECK
# ------------------------------
print("🚨 Missing Values:")
missing = df.isnull().sum()
print(missing[missing > 0], "\n")

# Visual
plt.figure(figsize=(8, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Value Heatmap")
plt.show()

# ------------------------------
# 2. DUPLICATES
# ------------------------------
duplicate_rows = df[df.duplicated()]
print(f"📦 Duplicate Rows: {len(duplicate_rows)}")
print(duplicate_rows.head(), "\n")

# ------------------------------
# 3. NEGATIVE VALUES CHECK
# ------------------------------
numeric_cols = ['Age', 'Salary']
for col in numeric_cols:
    if (df[col] < 0).any():
        print(f"❌ Invalid (Negative) values in '{col}':")
        print(df[df[col] < 0][[col]])
        print()

# ------------------------------
# 4. OUTLIERS DETECTION (Z-score)
# ------------------------------
from scipy.stats import zscore

z_scores = df[numeric_cols].apply(zscore)
outliers = (np.abs(z_scores) > 3)

print("📊 Outlier Summary:")
for col in numeric_cols:
    count = outliers[col].sum()
    print(f"{col}: {count} outliers")

# Boxplots for visualization
for col in numeric_cols:
    sns.boxplot(data=df[col])
    plt.title(f"Boxplot for {col}")
    plt.show()

# ------------------------------
# 5. PERFORMANCE SCORE INSPECTION
# ------------------------------
print("\n📈 Performance Score Distribution:")
sns.histplot(df['PerformanceScore'], bins=15, kde=True)
plt.title("Performance Score Distribution")
plt.show()

# Detect unusual scores (e.g., greater than 10)
if (df['PerformanceScore'] > 10).any():
    print("⚠️ Abnormally high Performance Scores detected:")
    print(df[df['PerformanceScore'] > 10])

# ------------------------------
# 6. INTERACTIVE VISUALS
# ------------------------------
fig = px.scatter(df, x="Age", y="Salary", color="Department", title="Age vs Salary (Colored by Department)")
fig.show()

fig2 = px.box(df, x="Department", y="Salary", color="Department", title="Salary Distribution per Department")
fig2.show()
