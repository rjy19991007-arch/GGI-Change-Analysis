import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# =========================
# 1. Load data
# =========================
# NOTE: Ensure the file is in the same directory as this script
file = "GGI.csv"
df = pd.read_csv(file)

# =========================
# 2. Specify column names
# NOTE: Make sure these column names match your dataset
# =========================
gray_col = "change_gray"
green_col = "change_green"

gray = df[gray_col].dropna()
green = df[green_col].dropna()

# =========================
# 3. Calculate statistical metrics
# =========================
def calculate_statistics(data):
    return {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Std": np.std(data),
        "MAD": np.median(np.abs(data - np.median(data))),
        "Skewness": skew(data),
        "Kurtosis": kurtosis(data),
        "Outlier_ratio": np.mean(np.abs(data - np.mean(data)) > 3 * np.std(data))
    }

gray_stats = calculate_statistics(gray)
green_stats = calculate_statistics(green)

summary = pd.DataFrame([gray_stats, green_stats], index=["Delta_Gray", "Delta_Green"])

# Save summary table
summary.to_csv("Distribution_stats.csv", index=True)

print(summary)

# =========================
# 4. Visualization (boxplot)
# =========================
plt.figure(figsize=(6, 5))

plt.boxplot([gray, green], labels=["Delta Gray", "Delta Green"])

plt.title("Distribution Comparison of Gray and Green Infrastructure Changes")
plt.ylabel("Change Value")

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

# Save figure
plt.savefig("Distribution_boxplot.png", dpi=300)

plt.show()
