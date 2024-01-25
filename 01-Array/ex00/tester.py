from give_bmi import give_bmi, apply_limit

def main():
	test = [8.1, 1.0]
	hlist = ["2.71", "1.15"]
	height = [2.71, 1.15, 1.68]
	weight = [165.3, 38.4]

	bmi = give_bmi(height, weight)
	print(bmi, type(bmi))
	limit = apply_limit(bmi, 8.0)
	print(limit)

if __name__ == "__main__":
	main()