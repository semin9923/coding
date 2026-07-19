def solution(n, numlist):
    answer = []
    for j in range(0, len(numlist)):
        if numlist[j] % n != 0:
            pass
        elif numlist[j] % n == 0:
            answer.append(numlist[j])
    return answer