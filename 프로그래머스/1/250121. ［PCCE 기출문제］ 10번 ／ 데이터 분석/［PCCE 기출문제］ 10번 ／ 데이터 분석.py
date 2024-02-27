def solution(data, ext, val_ext, sort_by):
    
    ext_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext = ext_dict[ext]
    sort_by = ext_dict[sort_by]
    
    new_data = []
    
    for i in data:
        if int(i[ext]) < int(val_ext):
            new_data.append(i)
    
    new_data = sorted(new_data, key = lambda x:x[sort_by], reverse = False)
        
    return new_data