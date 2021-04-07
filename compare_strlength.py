def compare_strlength(str1, str2):
    # YOUR CODE HERE
    return len(str1) == len(str2)

if __name__ == "__main__":
    str1, str2 = input().split()
    result = compare_strlength(str1, str2)
    # YOUR CODE HERE
    print(result)
