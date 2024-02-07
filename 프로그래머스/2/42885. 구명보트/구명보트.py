from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    people = deque(people)
    
    while True:
        max = people.popleft()
        
        # 남아 있는 사람이 0명일 경우 pop 방지
        if len(people) >= 1:
            min = people.pop()
            
            # limit보다 초과할 경우, 다시 deque에 삽입
            if max + min > limit:
                people.append(min)
                
        answer += 1
        
        # 사람이 없으면 반복문 탈출
        if len(people) == 0:
            break
            
    return answer