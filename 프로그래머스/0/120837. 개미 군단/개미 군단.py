def solution(hp):
    answer = 0
    # 횟수가 몫
    # 남은피가 나머지
    
    answer += (hp // 5)
    hp = hp % 5
    
    answer += (hp // 3)
    hp = hp % 3
    
    answer += hp
    
    
    return answer