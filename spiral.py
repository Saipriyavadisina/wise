j = 1
sum = 1
for i in range(1, 501):
    for k in range(4):
        j += 2 * i
        sum += j
print(sum)
