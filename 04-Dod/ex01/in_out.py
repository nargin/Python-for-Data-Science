def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0
    y = x

    def inner() -> float:
        nonlocal count, y
        count += 1
        y = function(y)
        return y

    return inner
