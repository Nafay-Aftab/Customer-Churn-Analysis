# 📊 Customer Churn Analysis 🔍

---

## 📄 Project Overview

This project analyzes customer churn within a telecommunications company using a dataset containing customer demographics, account details, and subscribed services. The objective is to uncover patterns and factors influencing customer churn and provide actionable insights for improving customer retention.

---

## 🗂 Table of Contents

- Technologies Used  
- Dataset  
- Data Cleaning and Preprocessing  
- Visualizations  
- How to Run  
- Analysis Insights  
- License  
- Notes for Users  
- Conclusion  

---

## 🛠 Technologies Used

- 🐍 **Python** — Core programming language used  
- 📊 **Pandas** — For data manipulation and preprocessing  
- 📈 **Seaborn** — Advanced statistical data visualization  
- 🖼 **Matplotlib** — Customizable plotting library  
- 📝 **Jupyter Notebook** — Interactive notebook environment

---

## 🗃 Dataset

The dataset `Customer Churn.csv` contains:

- **Demographics**: Gender, age, senior citizen status  
- **Account Info**: Tenure, contract type, payment method  
- **Service Details**: Subscriptions such as OnlineSecurity, TechSupport, StreamingTV  
- **Target**: `Churn` column (Yes/No) — whether the customer has churned

---

## 🧹 Data Cleaning and Preprocessing

- Handled missing values in `TotalCharges` by filling with `0`  
- Converted numeric categorical fields (e.g., `SeniorCitizen`) into readable labels  
- Encoded binary service columns (`Yes/No`) for easier plotting

---

## 📊 Visualizations

This notebook includes the following insights visualized using plots:

1. **Churn Distribution**  
   - Shows total customers who churned vs. retained  
   - Helps measure the imbalance in target variable

2. **Senior Citizens vs Non-Senior Citizens**  
   - Compares churn behavior by age group  
   - Indicates higher churn in senior citizens

3. **Churn by Tenure**  
   - Visualizes how long-term customers behave differently  
   - Short-tenure customers churn more

4. **Contract Type vs Churn**  
   - Bar chart comparing churn across Month-to-month, One-year, and Two-year contracts  
   - Month-to-month has highest churn

5. **Payment Method Impact**  
   - Electronic checks are most associated with high churn

6. **Service Subscriptions Impact**  
   - Count plots for services like:
     - `TechSupport`
     - `StreamingTV`
     - `OnlineSecurity`  
   - Shows customers with no added services tend to leave

> 🔍 *All plots are saved inside the `/images` folder.*

---

## 💻 How to Run

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Nafay-Aftab/Customer-Churn-Analysis.git

2. **Install Required Libraries**
   pip install pandas seaborn matplotlib jupyter

3. **Launch Jupyter Notebook**
   jupyter notebook

4. **Run the Notebook**
   Open Customer_Churn_Analysis.ipynb
   Make sure Customer Churn.csv is in the same folder
   Run all cells to generate plots and insights
   
---
   
   ### 🙋‍♂️ About Me
I'm a university student practicing Data Science by working on real-world datasets. This project is part of my learning journey where I apply concepts of data wrangling and visualization.
Let’s connect on LinkedIn and grow together!

LinkedIn: [Nafay Aftab](https://www.linkedin.com/in/muhammad-nafay-aftab-233138346/)
   






  
