def solution(s):
    s = list(s)
    stack = []
    
    for i in s:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()   # 같으면 제일 뒤에꺼 삭제
            else:
                stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0
            

# 시간 초과

# def solution(s):
#     s = list(s)
#     answer = 1
    
    
#     while len(s) != 0:
#         before_len = len(s)
#         for i in range(before_len - 1):
#             if s[i] == s[i+1]:
#                 s.pop(i+1)
#                 s.pop(i)
#                 break
                
#         after_len = len(s)
        
#         if before_len == after_len:
#             answer = 0
#             break

#     return answer