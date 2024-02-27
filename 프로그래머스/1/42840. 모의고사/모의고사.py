def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == student_1[i%5]:
            score_1 += 1
        if answers[i] == student_2[i%8]:
            score_2 += 1
        if answers[i] == student_3[i%10]:
            score_3 += 1
    
    result = max(score_1, score_2, score_3)
    
    answer = []
    
    if score_1 == result:
        answer.append(1)
    if score_2 == result:
        answer.append(2)
    if score_3 == result:
        answer.append(3)
    
    return answer