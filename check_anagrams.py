def check_anagrams(string1, string2):
    # YOUR CODE HERE
    return sorted(list(string1)) == sorted(list(string2))

if __name__ == "__main__":
    string1, string2 = input().split()
    result = check_anagrams(string1, string2)
    # YOUR CODE HERE
    print(result)


