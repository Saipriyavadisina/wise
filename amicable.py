def divisor_sum(x):
    sum = 0
    for j in range(1, x // 2 + 1):
        if x % j == 0:
            sum += j
    return sum

total_sum = 0
for i in range(10000):
    if divisor_sum(divisor_sum(i)) == i and divisor_sum(i) != i:
        total_sum += i
print(total_sum)
