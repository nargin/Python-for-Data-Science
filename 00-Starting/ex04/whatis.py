import sys


def is_valid_integer(s):
    if s.startswith(('+', '-')):
        return s[1:].isdigit()
    return s.isdigit()

def main():
    len_args = len(sys.argv)
    if len_args == 1:
        return 0

    try:
        assert len_args == 2, "more than one argument is provided"

        owo = sys.argv[1]
        assert is_valid_integer(owo), "argument is not an integer"
        owo = int(owo)

    except AssertionError as e:
        print("AssertionError:", e)
        return 1

    match owo % 2:
        case 0:
            print("I'm Even.")
        case 1:
            print("I'm Odd.")
    return 0


if __name__ == "__main__":
    main()
