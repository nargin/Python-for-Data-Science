from load_csv import load
import matplotlib.pyplot as plt

def main():
	csv = load("population_total.csv")

	country_names = []
	country_names.append("France")
	country_names.append("China")

	for country in country_names:
		country_data = csv[csv['country'] == country]

		if country_data.empty:
			print("Country not valid")
			return 1
		
		start_year = 1800
		end_year = 2050
		diff = end_year - start_year

		years = country_data.columns[1:]
		pop = country_data.iloc[0, 1:]

		years = years[:diff]
		pop = pop[:diff]

		plt.plot(years, pop, label=country)
	
	plt.xlabel("Year")
	plt.ylabel("Population (y)")
	plt.title("Population projections")

	plt.legend(loc="lower right")

	plt.yticks(pop[::20_000_000])
	plt.xticks(years[::40])

	plt.savefig("population.png")



if __name__ == "__main__":
	main()