import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Thomas Charette/Downloads/macro_monthly.csv")
df["DATE"] = pd.to_datetime(df["DATE"])
corr_matrix = df[["unrate","psr", "ir"]]
corr_matrix.columns = ["Unemployment Rate", "Personal Savings Rate", "Interest Rates"]
correlation_matrix = corr_matrix.corr()
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, square=True, linewidths=.5)

plt.title("Correlation Matrix")
plt.tight_layout()

plt.show()