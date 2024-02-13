import pandas as pd

def solution(genres, plays):
    df = pd.DataFrame({'genres': genres, 'plays': plays})
    # print(df)
    
    total = df.groupby(['genres'], as_index = False).sum()
    total.columns = ['genres', 'total']
    # print(total)
    
    df = pd.merge(df, total, how = 'left')
    # print(df)
    
    df = df.sort_values(['total', 'plays'], ascending = False)
    df = df.reset_index()
    # print(df)
    
    answer = []
    now_genres = str('')
    before_genres = str('')
    count = 0
    
    for i in range(len(df)):
        now_genres = df['genres'][i]
        count += 1
        
        if before_genres == now_genres:
            if count < 3:
                answer.append(int(df['index'][i]))
        else:
            answer.append(int(df['index'][i]))
            before_genres = now_genres
            count = 1
                
    return answer
        