import string
from collections import deque

def solution(msg):
    lzw_dict = {}
    dict_num = 0
    for i in string.ascii_uppercase:
        dict_num += 1
        lzw_dict[i] = dict_num
    
    answer = []
    
    while msg:
        temp_msg = ""
        
        for i in range(len(msg)):        	
            temp_msg += msg[i]  # 새로운 단어 만들기
            
            if temp_msg not in lzw_dict:    # 입력이 사전에 없는 경우 새로 저장
                dict_num += 1                
                lzw_dict[temp_msg] = dict_num                

                temp_msg = temp_msg[:-1]    # 이전 단어의 색인 출력
                answer.append(lzw_dict[temp_msg])                
                break
                
        # msg 초기화        
        msg = msg[len(temp_msg):]     
    
        # 마지막 단어가 사전에 있는 경우        
        if not msg:            
            answer.append(lzw_dict[temp_msg])
        
    return answer