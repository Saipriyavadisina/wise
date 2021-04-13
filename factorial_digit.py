def factorial(n):

    k = 1
    for m in range(1, n + 1):
        k *= m

    return k


def sum_of_digits(m):

    return sum([int(n) for n in str(m)])


print(sum_of_digits(factorial(100)))
