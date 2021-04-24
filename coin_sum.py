counts = {}
def sum_count(x, previous):
    if x == 1 or x == 0:
        return 1
    ways = 0
    for i in [200, 100, 50, 20, 10, 5, 2, 1]:
        if x >= i and previous >= i:
            ways += sum_count(x - i, i)
    counts[(x - 1, i)] = ways
    return ways


print(sum_count(200, 1000))
