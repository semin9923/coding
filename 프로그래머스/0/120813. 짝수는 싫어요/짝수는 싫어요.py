def solution(n):
    answer = []
    for j in range(0, n+1):
        if j % 2 != 0:
            answer.append(j)
    return answer