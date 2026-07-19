def solution(numbers):
    sum = 0
    for j in numbers:
        sum += j # sum = sum + j
    answer = sum / len(numbers)

    return answer