📊 Customer Churn Analysis 🔍


📄 Project Overview
This project aims to analyze customer churn within a telecommunications company using a dataset containing customer demographics, services, and account information. The goal is to identify patterns and factors contributing to customer churn and provide insights to improve retention strategies..

🗂 Table of Contents
Technologies Used
Dataset
Visualizations
How to Run
Analysis Insights
License

🛠 Technologies Used
🐍 Python: Main programming language for data analysis and visualization.
📊 Pandas: Data manipulation and analysis library.
📈 Seaborn: For advanced data visualization.
🖼 Matplotlib: For basic visualizations and plotting.
📝 Jupyter Notebook: Interactive environment for running and documenting the analysis.

🗃 Dataset
The dataset Customer Churn.csv includes the following features:
Customer Demographics: Age, gender, senior citizen status.
Account Information: Tenure, contract type, payment method.
Service Subscriptions: Whether the customer has subscribed to services like OnlineSecurity, TechSupport, StreamingTV, etc.
Target Variable: Churn (Yes/No) — indicates whether the customer has churned or stayed.


🧹 Data Cleaning and Preprocessing
Missing values in TotalCharges are replaced with 0.

Columns like SeniorCitizen are transformed into categorical labels (Yes/No) for easier analysis.

📊 Visualizations:
This project includes several visualizations to help understand customer churn patterns:
Churn Distribution: A bar chart showing the count and percentage of customers who churned vs. those who stayed.
Senior Citizens vs Non-Senior Citizens Churn: Insights into churn based on senior citizen status.
Churn by Tenure: How customer tenure impacts churn.
Contract Type Churn Analysis: Comparison of churn based on contract types.
Payment Method Churn: Analysis of churn patterns based on payment methods.
Service Subscription Impact: Multiple countplots showing churn behavior across various services like PhoneService, TechSupport, StreamingTV, etc.
All visualizations are saved in the /images folder.

💻 How to Run:
Clone the Repository:
git clone https://github.com/your-username/Customer-Churn-Analysis.git

Install Required Libraries:
Ensure you have the necessary Python libraries installed:
pip install pandas seaborn matplotlib jupyter

Open Jupyter Notebook:
jupyter notebook

Run the Notebook:
Open Customer_Churn_Analysis.ipynb in Jupyter and execute all cells to perform the analysis and generate visualizations.

Data File:
Make sure the Customer Churn.csv file is in the same directory as the notebook.

📈 Analysis Insights:

Churn Distribution: The analysis shows the overall churn rate and breaks it down by contract types, payment methods, and other factors.
Senior Citizens: Senior citizens display a distinct churn pattern when compared to non-senior citizens.
Tenure: Customers with shorter tenures tend to have higher churn rates.
Contract Type: Month-to-month contracts are linked to higher churn rates compared to longer-term contracts.
Payment Method: Customers using electronic checks tend to churn at higher rates.
Service Subscriptions: Subscriptions to services like TechSupport, StreamingTV, and OnlineSecurity have a significant effect on churn.

📝 License:
This project is open-source and intended for educational purposes. Feel free to fork or contribute to the repository.


💡 Notes for Users:
Customization: The notebook allows you to easily modify and explore additional analyses or add more features to the dataset.

Improvements: You can extend the analysis by applying machine learning models or incorporating feature engineering techniques to predict customer churn more accurately.


🎯 Conclusion:
This analysis helps us understand which factors contribute to customer churn, giving insights that can help businesses design retention strategies, such as offering targeted discounts, personalized services, or better contract terms, to reduce churn and improve customer loyalty.

