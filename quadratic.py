def check_prime(x):
    if x < 0:
        return False
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


most_primes = 0
highest_product = 1
for a in range(-999, 1000):
    for b in range(2, 1000):
        if check_prime(b):
            composite_found = False
            j = -1
            while not composite_found:
                j += 1
                if not check_prime((j ** 2) + a * j + b):
                    composite_found = True
            if j > most_primes:
                most_primes = j
                highest_product = a * b
print(highest_product)
