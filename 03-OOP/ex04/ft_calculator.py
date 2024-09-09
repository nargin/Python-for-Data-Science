def validate_vectors(func):
    """Decorator to validate the vectors"""
    def wrapper(V1: list[float], V2: list[float]):
        """Validate the vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise ValueError("Vectors must be lists")
        if not all(isinstance(x, (int, float)) for x in V1) or not all(
            isinstance(x, (int, float)) for x in V2
        ):
            raise ValueError("Vectors must contain only numbers")
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        return func(V1, V2)
    return wrapper


class calculator:
    """Vector calculator"""

    @staticmethod
    @validate_vectors
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Return the dot product of two vectors"""
        print(sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    @validate_vectors
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Return the sum of two vectors"""
        print([V1[i] + V2[i] for i in range(len(V1))])

    @staticmethod
    @validate_vectors
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Return the difference of two vectors"""
        print([V1[i] - V2[i] for i in range(len(V1))])
