import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# =========================
# 1. 读取数据
# =========================
file = r"E:\K\城市群\修改\GGI_CHANGE\GGI1520.csv"
df = pd.read_csv(file)

# =========================
# 2. 指定字段（你需要确认列名）
# =========================
gray_col = "change15_20_gray"
green_col = "change15_20_green"

gray = df[gray_col].dropna()
green = df[green_col].dropna()

# =========================
# 3. 计算统计指标
# =========================
def calc_stats(data):
    return {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Std": np.std(data),
        "MAD": np.median(np.abs(data - np.median(data))),
        "Skewness": skew(data),
        "Kurtosis": kurtosis(data),
        "Outlier_ratio": np.mean(np.abs(data - np.mean(data)) > 3*np.std(data))
    }

gray_stats = calc_stats(gray)
green_stats = calc_stats(green)

summary = pd.DataFrame([gray_stats, green_stats], index=["ΔGray", "ΔGreen"])

# 保存表
summary.to_csv(r"E:\K\城市群\修改\GGI_CHANGE\Distribution_stats1520.csv")

print(summary)

# =========================
# 4. 画图（箱线图）
# =========================
plt.figure(figsize=(6,5))

plt.boxplot([gray, green], labels=["ΔGray", "ΔGreen"])

plt.title("Distribution comparison of ΔGray and ΔGreen")
plt.ylabel("Change value")

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig(r"E:\K\城市群\修改\GGI_CHANGE\Distribution_boxplot1520.png", dpi=300)

plt.show()