import numpy as np
import pandas as pd
def solution (genres, plays):
    musics = pd. DataFrame ()
    musics ['id'] = range (len (plays) )
    musics ['plays'] = plays
    musics ['genres'] = genres
    musics ['genres_plays'] = musics.groupby ('genres').transform(np.sum)['plays']
    musics['genres_head_id'] = musics.groupby ('genres'). transform(np.min) ['id']
    musics ['order'] = musics['genres_plays']*1000000 - musics['genres_head_id' ]*1000 + musics['plays']
    answer = musics.sort_values('order', ascending=False).groupby('genres').head(2)['id']
    answer = list (answer)
    return answer