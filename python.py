
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
