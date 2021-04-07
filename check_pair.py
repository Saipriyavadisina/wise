def check_pair(string1, string2):
    # YOUR CODE HERE
    return string1[0] == string2[-1] and string1[-1] == string2[0]

if __name__ == "__main__":
    string1, string2 = input().split()
    result = check_pair(string1, string2)
    # YOUR CODE HERE
    print(result)
