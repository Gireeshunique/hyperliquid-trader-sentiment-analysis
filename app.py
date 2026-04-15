import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Advanced Trader Analytics Dashboard")

df = pd.read_csv("D:\\Project_ds\\merged_data.csv")

# KPIs
st.metric("Total Trades", len(df))
st.metric("Avg PnL", round(df['pnl'].mean(),2))

# =====================
# Prediction Section
# =====================
st.subheader("🤖 Profit Prediction")

size = st.slider("Position Size", float(df['size_usd'].min()), float(df['size_usd'].max()))
sentiment = st.selectbox("Sentiment", ['Fear','Greed'])

sentiment_num = 0 if sentiment == 'Fear' else 1

# simple rule (since model not loaded here)
prediction = "Profit Likely" if size < df['size_usd'].mean() else "Risky Trade"

st.write("Prediction:", prediction)

# =====================
# Clustering Section
# =====================
st.subheader("🧠 Trader Clusters")

cluster_df = df.groupby('account').agg({
    'pnl':'mean',
    'size_usd':'mean'
}).reset_index()

fig, ax = plt.subplots()
sns.scatterplot(data=cluster_df, x='size_usd', y='pnl', ax=ax)
st.pyplot(fig)