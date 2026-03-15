import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display first rows
print(data.head())

# Dataset Information
print(data.info())

# Statistical Summary
print(data.describe())

# Check Missing Values
print(data.isnull().sum())

# Clean column names
data.columns = data.columns.str.strip()

# Convert Date column
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

data.columns = data.columns.str.strip()

data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Bar Plot: Unemployment Rate by Region
plt.figure(figsize=(10,6))
sns.barplot(x="Region", y="Estimated Unemployment Rate (%)", data=data)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.show()

# Line Plot: Unemployment Trend
plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate (%)", data=data)
plt.title("Unemployment Rate Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# Scatter Plot: Labour Participation vs Unemployment
plt.figure(figsize=(8,6))
sns.scatterplot(
    x="Estimated Labour Participation Rate (%)",
    y="Estimated Unemployment Rate (%)",
    hue="Region",
    data=data
)
plt.title("Labour Participation vs Unemployment Rate")
plt.show()

# Box Plot: Distribution of Unemployment Rate
plt.figure(figsize=(10,6))
sns.boxplot(x="Region", y="Estimated Unemployment Rate (%)", data=data)
plt.xticks(rotation=90)
plt.title("Distribution of Unemployment Rate by Region")
plt.show()

# Heatmap
pivot = data.pivot_table(
    values="Estimated Unemployment Rate (%)",
    index="Region",
    columns="Date"
)

plt.figure(figsize=(12,7))
sns.heatmap(pivot, cmap="coolwarm")
plt.title("Heatmap of Unemployment Rate")
plt.show()
