import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Generate realistic synthetic data
# -----------------------------
np.random.seed(42)

# Customer Acquisition Cost (50–500 dollars)
cac = np.random.uniform(50, 500, 200)

# Customer Lifetime Value (positively correlated with CAC)
clv = cac * np.random.uniform(8, 12) + np.random.normal(0, 500, 200)

df = pd.DataFrame({
    "CAC": cac,
    "CLV": clv
})

# -----------------------------
# Styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # makes chart presentation-ready

# 512x512 output → figsize (8,8) with dpi=64
plt.figure(figsize=(8, 8))

# -----------------------------
# Scatterplot
# -----------------------------
sns.scatterplot(
    data=df,
    x="CAC",
    y="CLV",
    palette="viridis",
    hue="CAC",      # color scale based on CAC
    s=80,           # point size
    edgecolor="black"
)

plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=18)
plt.xlabel("Customer Acquisition Cost (USD)")
plt.ylabel("Customer Lifetime Value (USD)")

# -----------------------------
# Save chart with exact size
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
