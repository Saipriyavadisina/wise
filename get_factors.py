def get_factors(n):
    # YOUR CODE HERE
def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

if __name__ == "__main__":
    n = int(input())
    result = get_factors(n)
    # YOUR CODE HERE