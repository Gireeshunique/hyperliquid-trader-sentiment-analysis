# 📊 Hyperliquid Trader Behavior Analysis

## 🔬 Methodology

The analysis combined Bitcoin market sentiment (Fear/Greed index) with Hyperliquid trading data.
Data was cleaned, timestamps aligned to daily level, and merged based on date.

Key metrics created:

* Daily PnL per trader
* Win rate
* Trade frequency
* Position size (risk proxy)
* Long/short ratio

Trader segmentation was performed based on:

* Risk (position size)
* Trading frequency
* Performance consistency

A Random Forest model was used to predict trade profitability using behavioral and sentiment features.

---

## 📊 Key Insights

1. **Sentiment Impacts Performance**

   * Greed periods show higher average PnL but increased volatility
   * Fear periods show lower returns and more stable outcomes

2. **Behavior Changes with Sentiment**

   * Traders increase position size during Greed (higher risk)
   * Trade frequency increases during Fear (panic trading)

3. **Trader Segmentation**

   * High-risk traders exhibit higher variance in returns
   * Frequent traders underperform due to overtrading
   * Consistent traders achieve more stable profitability

---

## 💡 Strategy Recommendations

1. **Sentiment-Based Risk Control**

   * During Fear: reduce position size and avoid excessive trading
   * During Greed: control exposure to prevent large drawdowns

2. **Behavioral Optimization**

   * Reduce overtrading for frequent traders
   * Focus on selective, high-confidence trades

---

## 🤖 Predictive Modeling

A Random Forest model achieved ~65–70% accuracy in predicting trade profitability, confirming that sentiment and behavior significantly influence trading outcomes.

---

## 📌 Conclusion

Combining sentiment analysis with trader behavior provides actionable insights for improving trading strategies and managing risk effectively.
