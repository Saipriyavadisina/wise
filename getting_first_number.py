def function(n):
    i = 0
    while i < 20:
        if n % 2 == 0 and i % 2 == 1:
            return i *n
        i += 1
    return 42

print(function(4))
