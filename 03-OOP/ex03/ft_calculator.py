class calculator:
    """Vector calculator"""

    def __init__(self, keys: list) -> None:
        """Initiate the calculator with a list of keys"""
        if not isinstance(keys, list) or not all(
            isinstance(x, (int, float)) for x in keys
        ):
            raise ValueError("Keys must be a list")
        self.keys = keys

    def __add__(self, obj) -> None:
        """Add a number to the keys"""
        self.keys = [key + obj for key in self.keys]
        print(self.keys)

    def __sub__(self, obj) -> None:
        """Subtract a number from the keys"""
        self.keys = [key - obj for key in self.keys]
        print(self.keys)

    def __mul__(self, obj) -> None:
        """Multiply the keys by a number"""
        self.keys = [key * obj for key in self.keys]
        print(self.keys)

    def __truediv__(self, obj) -> None:
        """Divide the keys by a number"""
        try:
            self.keys = [key / obj for key in self.keys]
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        print(self.keys)
