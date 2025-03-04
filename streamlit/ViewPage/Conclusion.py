import streamlit as st
import pandas as pd

st.title("🏭 Clothing Sales Prediction - Conclusion Page")

# Problem Statement
st.subheader("📌 Problem Statement")
st.write(
    "A clothing manufacturing company wants to identify key attributes that contribute to high sales 📈. "
    "The goal is to build Decision Tree 🌳 and Random Forest 🌲 models to predict sales, "
    "with Sales as the target variable, which must first be converted into a categorical variable 🎯."
)

# Model Performance Comparison
st.subheader("🔥 Model Performance Comparison")

# Creating a DataFrame for model comparison
data = {
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Decision Tree 🌳": ["80.0%", "81.39%", "81.39%", "81.39%"],
    "Random Forest 🌲": ["87.5%", "88.37%", "88.37%", "88.37%"]
}
df = pd.DataFrame(data)

# Display the table
st.table(df)

# Why Random Forest is Better?
st.subheader("✅ Why is Random Forest Better?")
st.write("Random Forest outperforms Decision Tree in all metrics because:")
st.markdown(
    "- **Higher Accuracy 📈** (87.5% vs 80.0%)\n"
    "- **Better Precision, Recall & F1-Score 🎯** (More balanced and reliable)\n"
    "- **More Robust & Generalized ✅** (Reduces overfitting by averaging multiple trees)"
)

# Conclusion
st.subheader("🚀 Conclusion")
st.write(
    "Since Random Forest gives the best accuracy and overall balanced performance, it is the preferred model for predicting sales trends. "
    "This model can help the company make data-driven decisions to maximize sales and optimize marketing strategies effectively. 📊💡"
)
