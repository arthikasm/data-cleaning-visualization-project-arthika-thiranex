import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("StudentsPerformance.csv")

print("Dataset Loaded Successfully\n")

print("Checking Missing Values:")
print(df.isnull().sum())

print("\nChecking Duplicates:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nStatistical Summary:")
print(df.describe())

import os
os.makedirs("outputs", exist_ok=True)

gender_scores = df.groupby('gender')['math score'].mean()

plt.figure(figsize=(6,4))
gender_scores.plot(kind='bar')

plt.title("Average Math Score by Gender")
plt.ylabel("Math Score")
plt.tight_layout()

plt.savefig("outputs/gender_math_score.png")
plt.close()

plt.figure(figsize=(7,5))

plt.hist(df['math score'],
         bins=10)

plt.title("Math Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("outputs/score_distribution.png")
plt.close()

plt.figure(figsize=(6,4))

corr = df[['math score',
           'reading score',
           'writing score']].corr()

sns.heatmap(corr,
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("\nCharts Generated Successfully!")

df.to_csv("cleaned_data.csv",
          index=False)

print("\nProject Completed Successfully!")
