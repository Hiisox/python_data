from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter


def m_formatter(x, pos):
    return f'{x:.0f}M'


def main():
    data = load("population_total.csv")
    if data is None:
        return
    french_row = data[data['country'] == "France"]
    belgium_row = data[data['country'] == "Belgium"]
    nb_column = 0
    for x in range(0, french_row.shape[1]):
        if french_row.iloc[:, x].name != '2050':
            nb_column += 1
        else:
            nb_column += 1
            break
    french_values = [float(french_row.values[0][x][:-1]) for x in range(1, nb_column)]
    belgium_values = [float(belgium_row.values[0][x][:-1]) for x in range(1, nb_column)]
    year = [int(french_row.iloc[:,x].name) for x in range(1, nb_column)]
    
    plt.plot(year, french_values, label='France')
    plt.plot(year, belgium_values, label='Belgium')
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc='lower right')
    plt.title("Population Projections")
    plt.gca().xaxis.set_major_locator(MaxNLocator(7))
    plt.gca().yaxis.set_major_locator(MaxNLocator(4))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(m_formatter))
    plt.show()


if __name__ == "__main__":
    main()

