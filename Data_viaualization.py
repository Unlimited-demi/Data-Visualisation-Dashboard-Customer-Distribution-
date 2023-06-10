import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_dashboard():
    # Load the dataset
    df = pd.read_csv('Customers.csv')

    # Plotting gender distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender Distribution')
    plt.show()

    # Plotting age distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Age', bins=20, kde=True)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    plt.show()

    # Plotting annual income distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Annual Income', bins=20, kde=True)
    plt.xlabel('Annual Income')
    plt.ylabel('Count')
    plt.title('Annual Income Distribution')
    plt.show()

    # Plotting spending score distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Spending Score', bins=20, kde=True)
    plt.xlabel('Spending Score')
    plt.ylabel('Count')
    plt.title('Spending Score Distribution')
    plt.show()

    # Plotting profession distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, y='Profession')
    plt.xlabel('Count')
    plt.ylabel('Profession')
    plt.title('Profession Distribution')
    plt.show()

    # Plotting work experience distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Work Experience', bins=20, kde=True)
    plt.xlabel('Work Experience')
    plt.ylabel('Count')
    plt.title('Work Experience Distribution')
    plt.show()

    # Plotting family size distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Family Size')
    plt.xlabel('Family Size')
    plt.ylabel('Count')
    plt.title('Family Size Distribution')
    plt.show()

# Call the function to create the dashboard
create_dashboard()
