def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Limit the number of times a function can be called."""
        def limit_function(*args: any, **kwds: any):
            """Limit the number of times a function can be called."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called {limit}" +
                      (" times" if limit > 1 else " time"))
                return None

        return limit_function

    return callLimiter
