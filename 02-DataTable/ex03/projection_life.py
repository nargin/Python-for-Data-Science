from load_csv import load
import matplotlib.pyplot as plt


def main():
    life = load("life_expectancy_years.csv")
    pib = load("ipgpia.csv")

    for country in pib['country']:
        pib_data = pib[pib['country'] == country]
        life_data = life[life['country'] == country]

        if pib_data.empty or life_data.empty:
            print("Hmmm oO")
            return 1

        pib_number = pib_data.iloc[0, 1:]
        life_number = life_data.iloc[0, 1:]

        pib_number = pib_number[100:101]
        life_number = life_number[100:101]

        # print(pib_number)
        # print(life_number)

        plt.plot(pib_number, life_number, 'o')

    plt.xscale('log')
    plt.xticks([300, 1_000, 10_000], ['300', '1k', '10k'])

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")

    plt.savefig("pib.png")


if __name__ == "__main__":
    main()
