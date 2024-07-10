from load_csv import load
import matplotlib.pyplot as plt
from pandas import DataFrame


def aff_life(df:DataFrame):
    france_row = df[df['country'] == "France"]
    values = [france_row.values[0][x] for x in range(1, france_row.shape[1])]
    year = [int(france_row.iloc[:, x].name) for x in range(1, france_row.shape[1])]
    plt.plot(year, values)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()
    return


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    aff_life(data)
    return


if __name__ == "__main__":
    main()
