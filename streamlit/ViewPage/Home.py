import streamlit as st

# Title and Introduction
st.title("👕📈 Clothing Sales Prediction")
st.write(
    "This project builds Decision Tree 🌳 and Random Forest 🌲 models to identify key factors influencing high sales 📊 "
    "in a cloth manufacturing company 🏭, with sales converted into a categorical variable 🎯."
)

# CRISP Methodology
st.subheader("🔎 CRISP Methodology")
st.markdown(
    """✅ **Business & Data Understanding** 📊🔍  
    ✅ **Data Preparation** 🧹📂  
    ✅ **Model Building** 🤖⚙️  
    ✅ **Model Evaluation** 📈✅  
    ✅ **Model Deployment** 🚀💻  
    ✅ **Maintenance & Monitoring** 🛠️👀"""
)

# Business & Data Understanding
st.subheader("📂 Business & Data Understanding")
st.markdown("### 📌 Problem Statement")
st.write(
    "A cloth manufacturing company 🏭 wants to identify key attributes that contribute to high sales 📈. "
    "The goal is to build Decision Tree 🌳 and Random Forest 🌲 models, with Sales as the target variable, "
    "which must first be converted into a categorical variable 🎯."
)

# Business Objectives & Constraints
st.markdown("### 🎯 Business Objectives & Constraints")
st.write(
    """✅ **Business Objective:** Maximize profits 💰  
    ✅ **Business Constraint:** Minimize the time required to identify key attributes ⏳"""
)

# Success Criteria
st.markdown("### 📊 Success Criteria")
st.write(
    """📈 **Business Success Criteria:** Increase sales by 20%  
    🤖 **ML Success Criteria:** Achieve an accuracy of over 80%  
    💰 **Economic Success Criteria:** Ensure business profits exceed $3,000 USD"""
)

# Data Understanding
st.subheader("📂 Data Understanding")
st.write(
    "The dataset is provided by a trusted institute 🏛️ and contains:")
st.markdown("""✅ **11 Features** 📊  
✅ **400 Rows** 📝""")

# Feature Names & Descriptions
st.markdown("### 🔢 Feature Names & Descriptions")
data_features = {
    "Sales 📈": "Target variable, product sales",
    "CompPrice 💲": "Competitor's product price",
    "Income 💰": "Customer's annual income",
    "Advertising 📢": "Marketing budget spent",
    "Population 🌍": "Population in the area",
    "Price 🏷️": "Product selling price",
    "ShelveLoc 📌": "Shelf display location",
    "Age 🎂": "Customer’s age group",
    "Education 🎓": "Years of education",
    "Urban 🏙️": "Urban or rural location",
    "US 🇺🇸": "Customer in the US"
}
for feature, description in data_features.items():
    st.write(f"**{feature}** – {description}")

st.write("📌 Explore the other pages to dive deeper into the analysis!")