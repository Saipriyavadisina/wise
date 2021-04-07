def is_plural(word):
    # YOUR CODE HERE
    return word[-1] == 's'

if __name__ == "__main__":
    word = input()
    result = is_plural(word)
    # YOUR CODE HERE
    print(result)
