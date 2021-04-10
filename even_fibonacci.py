fibonacci_numbers = [0, 1]
for i in range(2,700):         
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
summ=0
for term in fibonacci_numbers:
    if term%2==0 and term<4000000:
        summ=summ+term
print(summ)

