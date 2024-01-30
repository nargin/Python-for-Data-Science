from load_csv import load
import matplotlib.pyplot as plt

def convert_data(array):
	converted_data = []

	for number in array:
		if 'K' in number:
			converted_data.append(float(number[:-1]) * 10**3)
		elif 'M' in number:
			converted_data.append(float(number[:-1]) * 10**6)
		elif 'B' in number:
			converted_data.append(float(number[:-1]) * 10**9)
		else:
			converted_data.append(number)
	return converted_data

def main():
	csv = load("population_total.csv")

	country_names = []
	country_names.append("France")
	country_names.append("Belgium")


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
		pop = convert_data(pop)
		
		plt.plot(years, pop, label=country)
		# for i, x in enumerate(pop):
		# 	print(f"{i}: {x}")
	
	plt.xlabel("Year")
	plt.ylabel("Population (y)")
	plt.title("Population projections")

	plt.legend(loc="lower right")

	plt.yticks(pop[::20_000_000])
	plt.xticks(years[::40])

	plt.savefig("population.png")



if __name__ == "__main__":
	main()