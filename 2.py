def function1(x, y):
    big, small = (x, y) if x > y else (y, x)

    leaves = big % small
    if not leaves == 0:
        return function1(small, leaves)
    else:
        return small






print(function1(-165, -3))


