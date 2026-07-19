def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
        
    for i in range(a, b+1): # a = 3 b = 5
        answer += i
    return answer

    if a == b:
        return a