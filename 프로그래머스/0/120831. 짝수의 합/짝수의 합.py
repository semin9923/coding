def solution(n):
    answer = 0
    for j in range(0, n+1, 1):
        if j % 2 == 0:
            answer += j
    return answer