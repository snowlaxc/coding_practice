import pandas as pd

def solution(friends, gifts):
    print(friends)
    print(gifts)
    
    df = pd.DataFrame(0, index = friends, columns = friends)
    gift = df.copy()
    
    for i in gifts:
        give, get = i.split(' ')
        df[get][give] += 1
        gift[get][give] += 1
        gift[give][get] -= 1
    
    gift_score = {}
    
    for i in friends:
        gift_score[i] = gift.loc[gift.index == i].sum().sum()
    
    # print(df)
    # print(gift_score)
    
    answer = {}
    
    for i in friends:
        for j in friends:
            if df[i][j] < df[j][i]:
                answer[i] = answer.get(i, 0) + 1
            if df[i][j] == df[j][i]:
                if gift_score[i] > gift_score[j]:
                    answer[i] = answer.get(i, 0) + 1
                    
    # print(answer)
    
    if not answer:
        return 0
    
    return max(answer.values())