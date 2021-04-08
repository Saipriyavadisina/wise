def is_pandigital(n):
    # YOUR CODE HERE
def is_pandigital_num(n):
    return len(set(str(n))) == 10

if __name__ == "__main__":
    n = int(input())
    result = is_pandigital(n)
    # YOUR CODE HERE