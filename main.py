from data import get_user_data
from plot import plot_income_expenditure

def main():
    info = get_user_data()
    plot_income_expenditure(info)

if __name__ == "__main__":
    main()
