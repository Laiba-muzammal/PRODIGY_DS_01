import pandas as pd

def get_user_data():
    data = {
        'Name': ['John', 'Alice', 'Bob', 'Emma', 'Chris', 'Sara', 'Michael', 'Olivia', 'James', 'Sophia'],
        'Age': [28, 34, 45, 23, 50, 37, 41, 29, 33, 39],
        'Income': [35000, 45000, 50000, 30000, 60000, 52000, 47000, 38000, 42000, 55000],
        'Expenditure': [15000, 25000, 40000, 22000, 35000, 40000, 30000, 28000, 39000, 47000]
    }
    return pd.DataFrame(data)
