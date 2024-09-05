def ft_filter(function, iterable):
    """ft_filter(function, iterable) --> filter object"""
    return [elem for elem in iterable if function(elem)]
