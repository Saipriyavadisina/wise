def generate_pattern(n):
    # YOUR CODE HERE
n = 4562
rev = 0
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)

if __name__ == "__main__":
    N = int(input())
    generate_pattern(N)