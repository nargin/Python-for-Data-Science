def ft_quartile(*args: any) -> float:
    """Returns the quartile of the given arguments."""
    if len(args) == 0:
        return None

    args = sorted(args)
    n = len(args)

    if n % 2 == 0:
        q1 = ft_median(*args[:n // 2])
        q3 = ft_median(*args[n // 2:])
    else:
        q1 = ft_median(*args[:n // 2])
        q3 = ft_median(*args[n // 2 + 1:])

    return q1, q3


def ft_mean(*args: any) -> float:
    """Returns the mean of the given arguments."""
    if len(args) == 0:
        return None

    return sum(args) / len(args)


def ft_variance(*args: any) -> float:
    """Returns the variance of the given arguments."""
    if len(args) == 0:
        return None

    c = 0
    s = args[0]
    n = len(args)

    for j in range(2, n + 1):
        xj = args[j - 1]
        s += xj
        c += ((j * xj - s) ** 2) / (j * (j - 1))

    return c / n


def ft_median(*args: any) -> float:
    """Returns the median of the given arguments."""
    if len(args) == 0:
        return None

    args = sorted(args)
    n = len(args)

    if n % 2 == 0:
        return (args[n // 2 - 1] + args[n // 2]) / 2
    else:
        return args[n // 2]


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the statistics of the given arguments."""

    for key, value in kwargs.items():
        if value == "var":
            var = ft_variance(*args)
            print(f"Variance: {var}") if var is not None else print("ERROR")
        elif value == "std":
            std = ft_variance(*args) ** 0.5
            print(f"Standard deviation: {std}") if std is not None else print(
                "ERROR")
        elif value == "mean":
            mean = ft_mean(*args)
            print(f"Mean: {mean}") if mean is not None else print("ERROR")
        elif value == "median":
            median = ft_median(*args)
            print(f"Median: {median}") if median is not None else print(
                "ERROR")
        elif value == "quartile":
            quartile = ft_quartile(*args)
            print(f"Quartile: {quartile}") if quartile is not None else print(
                "ERROR")
