from time import sleep
from tqdm import tqdm


def ft_tqdm(iterable: range):
    """ft_tqdm is a function that displays a progress\
    bar for an iterable object."""
    total = len(iterable)

    for i, item in enumerate(iterable):
        percent = (i + 1) / total * 100
        print(
            f'\r{int(percent)}%'
            f'[{"=" * int(percent)}>{" " * (100 - int(percent))}]'
            f' {i + 1}/{total}',
            end=''
        )
        yield item
    print()


def main():
    for _ in ft_tqdm(range(333)):
        sleep(0.01)
    for _ in tqdm(range(333)):
        sleep(0.01)


if __name__ == '__main__':
    main()
