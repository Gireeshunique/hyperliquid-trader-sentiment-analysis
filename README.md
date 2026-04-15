# 📊 Hyperliquid Trader Sentiment Analysis

## 📌 Overview

This project analyzes how **market sentiment (Fear vs Greed)** impacts trader behavior and performance on Hyperliquid.
It combines sentiment data with trading activity to uncover patterns and build smarter trading strategies.

---

## 🎯 Objective

* Understand relationship between sentiment and trader performance
* Analyze behavioral changes under different market conditions
* Build predictive models for profitability
* Provide actionable trading strategies

---
[▶️ Watch Demo](https://github.com/Gireeshunique/hyperliquid-trader-sentiment-analysis/blob/dc399fc46ca9f2aa496024890b61b16dbe0d9a8d/streamlit-app-2026-04-15-19-04-80.webm)

## 📂 Dataset

1. Bitcoin Fear/Greed Index
2. Hyperliquid Historical Trader Data

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Seaborn, Matplotlib
* Scikit-learn
* Streamlit

---

## 🔄 Workflow

### 1. Data Preparation

* Cleaned missing values and duplicates
* Converted timestamps to daily level
* Merged sentiment with trading data

### 2. Feature Engineering

* Daily PnL per trader
* Win rate
* Trade frequency
* Position size (risk proxy)
* Long/short ratio

---

## 📊 Analysis & Insights

### 📈 Performance vs Sentiment

* Greed → higher average PnL but higher volatility
* Fear → lower returns but more stability

### 🔄 Behavioral Patterns

* Traders take larger positions during Greed
* Trade frequency increases during Fear

### 🧠 Trader Segmentation

* High-risk traders → high variance returns
* Frequent traders → lower profitability (overtrading)
* Consistent traders → stable performance

---

## 💡 Strategy Recommendations

### ✅ Strategy 1 — Sentiment-Based Risk Control

* Fear → reduce position size, avoid overtrading
* Greed → control risk, avoid excessive exposure

### ✅ Strategy 2 — Behavioral Optimization

* Reduce overtrading for frequent traders
* Focus on high-quality trades

---

## 🤖 Machine Learning Model

* Model: Random Forest Classifier
* Accuracy: ~65–70%
* Features:

  * Position size
  * Sentiment
  * Trade frequency

👉 Insight: Profitability is influenced by both market sentiment and trader behavior

---

## 📊 Dashboard

A Streamlit dashboard is included to:

* Visualize sentiment vs performance
* Explore trader behavior
* View key metrics interactively

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Gireeshunique/hyperliquid-trader-sentiment-analysis.git
cd hyperliquid-trader-sentiment-analysis
```

### 2. Install Dependencies

```bash
pip install pandas numpy seaborn matplotlib scikit-learn streamlit
```

### 3. Run Notebook

Open:

```bash
notebook.ipynb
```

### 4. Run Dashboard

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
hyperliquid-trader-sentiment-analysis/
│
├── notebook.ipynb
├── app.py
├── merged.csv
├── README.md
├── report.md
└── images/
```

---

## 📌 Key Takeaway

Combining **market sentiment + trader behavior** provides powerful insights to improve trading performance and risk management.

---

## 🚀 Future Improvements

* Add time-series prediction (next-day PnL)
* Deploy dashboard online
* Enhance feature engineering
* Real-time data integration

---


Your Name
