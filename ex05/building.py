import sys
import string

def main():
	len_args = len(sys.argv)

	if len_args == 1:
		owo = input()
		len_args = 2
	else:
		owo = sys.argv[1]

	try :
		assert len_args == 2, "more than one argument is provided"
		assert owo != "", "empty string"
	except AssertionError as e:
		print("AssertionError:", e)
		return 1

	lower = sum(1 for c in owo if c.islower())
	upper = sum(1 for c in owo if c.isupper())
	numeric = sum(1 for c in owo if c.isnumeric())
	white = sum(1 for c in owo if c.isspace())
	ponct = sum(1 for c in owo if c in string.punctuation)

	print("The text contains", len(owo), "characters:")
	print("-", upper, "upper letters")
	print("-", lower, "lower letters")
	print("-", ponct, "punctuation marks")
	print("-", numeric, "digits")
	print("-", white, "spaces")

if __name__ == "__main__":
	main()