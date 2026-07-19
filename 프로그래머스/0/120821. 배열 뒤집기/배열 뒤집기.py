def solution(num_list):
    answer = []
    for j in range(len(num_list)-1, -1, -1):
        answer.append(num_list[j])
    return answer