def slice_me(family: list, start: int, end: int) -> list:
    """ return a slice of the family list, from index start to index end """
    try:
        assert len(family) > 0, "family list is empty"
        assert start >= 0, "start index must be greater than or equal to 0"
        assert end <= len(
            family), "end index must be less than or\
                equal to the length of the family list"
    except AssertionError as e:
        print(e)
        return []
    row = len(family)
    col = len(family[0])
    print(f"Old shape: ({row}, {col})")
    family = family[start:end]
    row = len(family)
    col = len(family[0])
    print(f"New shape: ({row}, {col})")

    return family
