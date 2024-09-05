from time import sleep
from ft_package import ft_tqdm


def main():
    for i in ft_tqdm(range(666)):
        sleep(0.01)


if __name__ == '__main__':
    main()
