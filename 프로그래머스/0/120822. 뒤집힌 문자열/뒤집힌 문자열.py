def solution(my_string):
    answer = ''
    for j in range(len(my_string)-1, -1, -1):
        answer += my_string[j]
    return answer

