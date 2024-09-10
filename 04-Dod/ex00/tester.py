from statistics import ft_statistics


def test_ft_statistics():
    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 18, 18, 75, 450, 450, 597, 597, 27474, 27474,
                  48575, 485755, hello="quartile", world="var")


if __name__ == "__main__":
    test_ft_statistics()
