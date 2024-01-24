from time import sleep
from tqdm import tqdm

def ft_tqdm(iterable: range):
	total = len(iterable)

	for i, item in enumerate(iterable):
		percent = (i + 1) / total * 100
		print(f'\r{int(percent)}%[{"=" * int(percent)}>{" " * (100 - int(percent))}] {i + 1}/{total}', end='')
		yield item
	print()

def main():
	for _ in ft_tqdm(range(333)):
		sleep(0.01)
	for _ in tqdm(range(333)):
		sleep(0.01)

if __name__ == '__main__':
	main()