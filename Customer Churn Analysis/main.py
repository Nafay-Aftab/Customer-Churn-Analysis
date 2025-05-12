# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Customer Churn.csv')

# Cleaning and preprocessing
df['TotalCharges'].fillna(0, inplace=True)  # Fill missing TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')  # Convert to numeric
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'}).astype('object')  # Make categorical

# ---------------------------------------
# 1. Churn Count and Percentage
# ---------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar plot for churn count
ax1 = sns.countplot(x='Churn', data=df, ax=axes[0])
axes[0].set_title('Count of the People Churned')
ax1.bar_label(ax1.containers[0])

# Pie chart for churn percentage
gb = df['Churn'].value_counts()
axes[1].pie(gb, autopct='%1.2f%%', labels=gb.index)
axes[1].set_title('Percentage of the People Churned')

plt.tight_layout()
plt.savefig('churn_count.png')
plt.show()

# Summary: Most customers stayed, but a significant proportion churned.

# ---------------------------------------
# 2. Senior Citizen Churn Analysis
# ---------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Count of SeniorCitizen by churn status
ax1 = sns.countplot(x='SeniorCitizen', data=df, ax=axes[0])
ax1.bar_label(ax1.containers[0])
axes[0].set_title('Count by SeniorCitizen')

# Pie chart for churned senior citizens
churned = df[df['Churn'] == 'Yes']
gb = churned['SeniorCitizen'].value_counts()
axes[1].pie(gb, autopct='%1.2f%%', labels=gb.index)
axes[1].set_title('Percentage of Churned Customers by SeniorCitizen Status')

plt.tight_layout()
plt.savefig('Senior_citizen_churn.png')
plt.show()

# Summary: Senior citizens churn at a higher rate relative to their total population.

# ---------------------------------------
# 3. Tenure vs Churn (Histogram)
# ---------------------------------------
sns.displot(data=df, x='tenure', bins=72, hue='Churn', height=5, aspect=2)
plt.title('Churn based on Tenure')
plt.savefig('tenure_churn.png')
plt.show()

# Summary: Newer customers tend to churn more; loyal long-term users tend to stay.

# ---------------------------------------
# 4. Contract Type and Churn
# ---------------------------------------
plt.figure(figsize=(6, 4))
ax = sns.countplot(x='Contract', data=df, hue='Churn')
ax.bar_label(ax.containers[0])
plt.title('Churn on the Basis of Contract')
plt.tight_layout()
plt.savefig('contract_churn.png')
plt.show()

# Summary: Month-to-month contracts see the highest churn.

# ---------------------------------------
# 5. Service Features and Churn (Subplots)
# ---------------------------------------
cols = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
n_col = 3
n_row = (len(cols) + n_col - 1) // n_col
fig, axes = plt.subplots(n_row, n_col, figsize=(20, n_row * 6))
axes = axes.flatten()

for i, col in enumerate(cols):
    ax = axes[i]
    sns.countplot(data=df, x=col, hue='Churn', ax=ax)
    ax.set_title(f'Countplot of {col}')
    ax.tick_params(axis='x', rotation=0)
    for container in ax.containers:
        ax.bar_label(container, fontsize=9)

# Remove unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.subplots_adjust(hspace=0.4)
plt.savefig('services_based_churns.png')
plt.show()

# Summary: Services like TechSupport and OnlineSecurity show strong correlation with churn behavior.

# ---------------------------------------
# 6. Payment Method and Churn
# ---------------------------------------
plt.figure(figsize=(10, 5)) 
ax = sns.countplot(x='PaymentMethod', data=df, hue='Churn')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title('Churn on the Basis of Payment Method')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('payment_method_churn.png')
plt.show()

# Summary: Electronic checks have a significantly higher churn rate than other payment methods.
