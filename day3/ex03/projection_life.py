from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    life_expectancy = load("life_expectancy_years.csv")
    if life_expectancy is None:
        return
    income = load("income_per_person.csv")
    if income is None:
        return
    income_data = income[['country', '1900']]
    life_expectancy_data = life_expectancy[['country', '1900']]
    merged_data = pd.merge(income_data, life_expectancy_data, on='country')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.xscale('log')
    plt.xlim(300, 10000)
    plt.xticks([300, 1000, 10000], ['300', '1000', '10000'])
    plt.scatter(merged_data['1900_x'].astype(float), merged_data['1900_y'].astype(float))
    plt.show()


if __name__ == "__main__":
    main()