from time import sleep

def ft_tqdm(iterable: range):
	"""ft_tqdm is a function that displays a progress bar for an iterable object."""
	total = len(iterable)

	for i, item in enumerate(iterable):
		percent = (i + 1) / total * 100
		print(f'\r{int(percent)}%[{"=" * int(percent)}>{" " * (100 - int(percent))}] {i + 1}/{total}', end='')
		yield item
	print()