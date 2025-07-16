import matplotlib.pyplot as plt

def plot_income_expenditure(info_df):
    plt.figure(figsize=(10, 6))

    # Histogram of Expenditure
    plt.hist(info_df['Expenditure'], color='skyblue', alpha=0.5, label='Expenditure', edgecolor='black')

    # Histogram of Income
    plt.hist(info_df['Income'], color='gold', alpha=0.5, label='Income', edgecolor='black')

    plt.title("Income vs Expenditure")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
