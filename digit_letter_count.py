def digit_letter_count(word):
    # YOUR CODE HERE
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
if __name__ == "__main__":
    word = input()
    result = digit_letter_count(word)
    # YOUR CODE HERE