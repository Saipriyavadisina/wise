def divs(num):
    divisors = set()
    if num in {1, 0}:
        return set()
    for i in range(2, round(num**0.5) + 1):
        if not num % i:
            divisors.update({i, num // i})
    return divisors.union({1})
ABS = [i for i in range(1, 28124) if sum(divs(i)) > i]
SUMS = set()
for I in ABS:
    for J in ABS:
        SUMS.add(I+J)
S = 0
for I in range(1, 28124):
    if I not in SUMS:
        S += I
print(S)
