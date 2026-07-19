def solution(array, height):
    answer = 0
    for j in array:
        if j > height:
            answer += 1
    return answer