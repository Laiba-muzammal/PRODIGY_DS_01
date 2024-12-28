import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'Chris', 'Sara', 'Michael', 'Olivia', 'James', 'Sophia'],
    'Age': [28, 34, 45, 23, 50, 37, 41, 29, 33, 39],
    'Income': [35000, 45000, 50000, 30000, 60000, 52000, 47000, 38000, 42000, 55000],
    'Expenditure': [15000, 25000, 40000, 22000, 35000, 40000, 30000, 28000, 39000, 47000] 
}

info = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
bar_width = 0.35
plt.hist(info['Expenditure'], color='skyblue', alpha=0.5, label='Expenditure', edgecolor='black')
plt.hist(info['Income'], color='yellow', label='Income',alpha=0.5, edgecolor='black')
plt.title("Income VS Expenditure ")
plt.xlabel("Income & Expenditure")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()

