from load_csv import load
import matplotlib.pyplot as plt


def main():
    csv = load("life_expectancy_years.csv")

    if csv.empty:
        return 1

    country_name = 'France'
    country_data = csv[csv['country'] == country_name]
    print(country_data)
    if country_data.empty:
        print("This country is not available")

    years = country_data.columns[1:]  # 0 is country
    life_expt = country_data.iloc[0, 1:]  # 0 is country_name
    plt.plot(years, life_expt, label=country_name)

    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (y)')
    plt.title(f'{country_name} - Life Expectancy')

    plt.legend()

    plt.xticks(years[::40])

    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
