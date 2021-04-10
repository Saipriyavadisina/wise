def solution(n):
    res = [i for i in range(n) if is_Armstrong(i)]
    return res[-1]

def is_Armstrong(n):
    tem, dig, sum = n, len(str(n)), 0
    while n > 0:
        rem = n % 10
        sum += rem ** dig
        n //= 10
    return tem == sum

print(solution(6))
