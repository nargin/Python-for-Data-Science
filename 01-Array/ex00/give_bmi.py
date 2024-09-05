LFT = "list can only be int or float types"


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ return a list of bmi values,\
                given a list of heights and a list of weights """
    try:
        print("length of height: ", len(height))
        print("length of weight: ", len(weight))
        assert len(height) == len(weight), "length differs between the 2 lists"
        list_type = height.__class__.__name__
        assert list_type == 'int' or list_type == 'float', LFT
        list_type = weight.__class__.__name__
        assert list_type == 'int' or list_type == 'float', LFT
    except AssertionError as e:
        print(e)
        return []

    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / height[i] ** 2)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ return a list of boolean values,\
        True if bmi is greater than limit, False otherwise """
    return [elem > limit for elem in bmi]
