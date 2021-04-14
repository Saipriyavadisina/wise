from itertools import takewhile

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


LIMIT = 10 ** 999
print(1 + sum(1 for _ in takewhile(lambda x: x < LIMIT, fibonacci())))
