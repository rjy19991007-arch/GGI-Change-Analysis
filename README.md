# GGI-Change-Analysis
Statistical considerations for threshold estimation of ΔGray and ΔGreen
# GGI Change Analysis

## 📌 Description
This repository contains the data and code used to analyze the distribution characteristics of changes in gray and green infrastructure (GGI).

The analysis focuses on comparing the statistical properties of:
- Gray infrastructure change (ΔGray)
- Green infrastructure change (ΔGreen)

Key statistical metrics include mean, median, standard deviation, median absolute deviation (MAD), skewness, kurtosis, and outlier ratio. A boxplot is also generated to visualize distribution differences.

---

## 📂 Repository Structure

- `GGI.csv`  
  Input dataset containing gray and green infrastructure change variables.

- `GGI_distribution.py`  
  Python script used for statistical analysis and visualization.

- `Distribution_stats.csv`  
  Output table summarizing statistical metrics for ΔGray and ΔGreen.

- `Distribution_boxplot.png`  
  Boxplot comparing the distribution of gray and green infrastructure changes.

---

## ⚙️ Requirements

Python 3.x with the following packages:

- pandas  
- numpy  
- matplotlib  
- scipy  

Install dependencies using:

```bash
pip install pandas numpy matplotlib scipy
