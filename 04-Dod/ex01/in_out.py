def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that applies function to x."""
    count = 0
    y = x

    def inner() -> float:
        nonlocal count, y
        count += 1
        y = function(y)
        return y

    return inner
