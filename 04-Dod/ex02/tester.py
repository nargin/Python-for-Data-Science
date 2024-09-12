from callLimit import callLimit


def test_callLimit():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


test_callLimit()
