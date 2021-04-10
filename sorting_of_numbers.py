def solution(A, n):
    res = [i for i in A if i % 2 != 0]
    return sorted(res)[1]
A = [3, 4, 8, 18, 373, 21, 7, 33]
print(solution(A, len(A)))
