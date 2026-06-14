import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print("First 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nSummary Statistics:")
print(df.describe())

plt.hist(df["math score"])
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Count")
plt.savefig("math_distribution.png")
plt.show()

df.groupby("gender")["math score"].mean().plot(kind="bar")
plt.title("Average Math Score by Gender")
plt.ylabel("Average Score")
plt.savefig("gender_comparison.png")
plt.show()

plt.boxplot(df["reading score"])
plt.title("Reading Score Boxplot")
plt.savefig("reading_boxplot.png")
plt.show()

df.to_csv("cleaned_student.csv", index=False)

print("\nProject Completed Successfully!")
