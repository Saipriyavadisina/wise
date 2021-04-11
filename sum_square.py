sumsquares = 0
squaressum = 0

for i in range(101):
    sumsquares = sumsquares + i * i
    squaressum = squaressum + i

squaressum = squaressum * squaressum

print(squaressum - sumsquares)
