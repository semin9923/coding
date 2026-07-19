def solution(a, b):
    answer = 0
    j = str(a) + str(b)
    
    if int(j) >= 2 * a * b:
        answer = int(j) #'912'
    else:
        answer = 2 * a * b
    return answer