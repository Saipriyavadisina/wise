def generate_pattern(n):
    # YOUR CODE HERE
for i in range(n):
    print(' '*(n-1), end='')
    
    print(' '.join(map(str, str(11**i))))

if __name__ == "__main__":
    N = int(input())
    generate_pattern(N)