def solution(n, words):
    time = 0    # 라운드 카운팅
    before = words[0][0]    # 전 단어의 끝단어 세팅 (초기값은 첫단어 첫글자)
    done = []    # 사용 단어 리스트
    
    error = 0    # 틀렸는지 확인
    result = [0,0]    # result 값 생성
    
    for _ in range(len(words)):    # 총 라운드 세팅
        time += 1
        i = words.pop(0)
        
        if before == i[0]:    # 끝말잇기가 정상 진행될 경우
            before = i[-1]    # 다음 라운드를 위해 끝단어 세팅
        else:
            error = 1
            break
        
        if i not in done:    # 이미 한 단어도 아닐 경우
            done.append(i)
        else:
            error = 1
            break
            
    if error == 1:    # 탈락할 경우
        result = [int(time % n), int((time + (n - 1)) // n)]    # result 값 세팅
        
        if result[0] == 0:
            result[0] = n
            
    return result