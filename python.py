import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
data_path = r"C:\Users\ASUS\OneDrive\Desktop\DataSet Employment.xlsx"
df = pd.read_excel(data_path)


# Set up a plot style
sns.set(style="whitegrid")

# 1. Histogram  
plt.figure(figsize=(6, 4))
sns.histplot(df["Employment Rate"], kde=True, color="skyblue", bins=10)
plt.title("Histogram of Employment Rate")
plt.xlabel("Employment Rate")
plt.ylabel("Frequency")
plt.show()

# 2. Bar Plot (Average Employment Rate by Region)
plt.figure(figsize=(6, 4))
sns.barplot(x="Region", y="Employment Rate", data=df, palette="Set2")
plt.title("Average Employment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Employment Rate")
plt.xticks(rotation=45)  # In case region labels are long
plt.show()

# 3. Scatter Plot (Employment Rate vs GDP)
plt.figure(figsize=(6, 4))
sns.scatterplot(x="GDP", y="Employment Rate", data=df, hue="Region", palette="coolwarm", s=100)
plt.title("Employment Rate vs GDP")
plt.xlabel("GDP")
plt.ylabel("Employment Rate")
plt.show()
