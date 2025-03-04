# 👕📈 Clothing Sales Prediction  

This project builds **Decision Tree** 🌳 and **Random Forest** 🌲 models to identify key factors influencing **high sales** 📊 in a **cloth manufacturing company** 🏭, with sales converted into a **categorical variable** 🎯.  

## 🚀 WorkFlow  
1️⃣ **Update** 🛠️ `config.yaml`  
2️⃣ **Update** 📜 `schema.yaml`  
3️⃣ **Update** ⚙️ `params.yaml`  
4️⃣ **Update** 🏗️ **the entity**  
5️⃣ **Update** 📝 **the configuration manager in `src/config`**  
6️⃣ **Update** 🧩 **the components**  
7️⃣ **Update** 🔄 **the pipeline**  
8️⃣ **Update** 🚀 `main.py`  
9️⃣ **Update** 🌐 `app.py`  

## 📌 **CRISP Methodology**  
✅ **Business & Data Understanding** 📊🔍  
✅ **Data Preparation** 🧹📂  
✅ **Model Building** 🤖⚙️  
✅ **Model Evaluation** 📈✅  
✅ **Model Deployment** 🚀💻  
✅ **Maintenance & Monitoring** 🛠️👀  

## 📂 **Business & Data Understanding**  

### 📌 **Problem Statement**  
A **cloth manufacturing company** 🏭 wants to identify key attributes that contribute to **high sales** 📈. The goal is to build **Decision Tree** 🌳 and **Random Forest** 🌲 models, with **Sales** as the **target variable**, which must first be **converted into a categorical variable** 🎯.  

### 🎯 **Business Objectives & Constraints**  
✅ **Business Objective:** Maximize profits 💰  
✅ **Business Constraint:** Minimize the time required to identify key attributes ⏳  

### 📊 **Success Criteria**  
- **📈 Business Success Criteria:** Increase sales by **20%**  
- **🤖 ML Success Criteria:** Achieve an accuracy of over **80%**  
- **💰 Economic Success Criteria:** Ensure business profits exceed **$3,000 USD**  

## 📂 **Data Understanding**  

The dataset is provided by a **trusted institute** 🏛️ and contains:  
- **11 features** 📊  
- **400 rows** 📝  

### 🔢 **Feature Names & Descriptions**  
- **Sales** 📈 – Target variable, product sales  
- **CompPrice** 💲 – Competitor's product price  
- **Income** 💰 – Customer's annual income  
- **Advertising** 📢 – Marketing budget spent  
- **Population** 🌍 – Population in the area  
- **Price** 🏷️ – Product selling price  
- **ShelveLoc** 📌 – Shelf display location  
- **Age** 🎂 – Customer’s age group  
- **Education** 🎓 – Years of education  
- **Urban** 🏙️ – Urban or rural location  
- **US** 🇺🇸 – Customer in the US

# 🚀 MLflow Tracking

MLflow is used to log experiments and track models with different parameters. Some key tracking features:

- 📊 **HyperParameters**: Logs values such as learning rate, batch size, etc.  
- 📈 **Metrics**: Records accuracy, F1-score, recall, and precision evaluation metrics.  

🚀🔥 **This is my tracking ID, click below to view it!**  

[![MLflow](https://img.shields.io/badge/MLflow-0250A3?style=for-the-badge&logo=mlflow&logoColor=white)](https://dagshub.com/revanth-kumar-01-ai/clothing-sales-prediction.mlflow)


# 📊 Model Performance Comparison

Below is the performance comparison between **Decision Tree** and **Random Forest** classifiers.

## 🔥 Model Performance Metrics

| Metric            | Decision Tree | Random Forest |
|------------------|--------------|--------------|
| **Accuracy**     | 0.800        | 0.875        |
| **Precision**    | 0.8139       | 0.8837       |
| **Recall**       | 0.8139       | 0.8837       |
| **F1-Score**     | 0.8139       | 0.8837       |

## ✅ Why Random Forest is Better?
Random Forest outperforms the Decision Tree in all metrics:
- **Higher Accuracy** 📈 (87.5% vs 80.0%)
- **Better Precision, Recall & F1-Score** 🎯
- **More Robust & Generalized** ✅ (Reduces overfitting by averaging multiple trees)

🚀 **Conclusion**: Since Random Forest gives the best accuracy and balanced performance, it is the preferred model for prediction tasks.
