def solution(n):
    answer = 0
    n = str(n)
    for j in n:
        answer = answer + int(j)
    return answer