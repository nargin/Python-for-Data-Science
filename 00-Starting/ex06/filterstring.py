import sys
from ft_filter import ft_filter

ARGS_ERROR = "the arguments are bad"


def main():
    args = sys.argv[1:]

    try:
        assert len(args) == 2, ARGS_ERROR
        assert args[1].isdigit(), ARGS_ERROR
        assert len(args[0]) > 0, ARGS_ERROR
    except AssertionError as e:
        print(e)
        return 1

    n = int(args[1])
    s = args[0]
    lst = list(ft_filter(lambda x: len(x) > n, s.split()))
    print(lst)
    return 0


if __name__ == "__main__":
    main()
