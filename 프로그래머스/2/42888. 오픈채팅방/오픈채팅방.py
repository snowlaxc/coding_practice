def solution(record):
    nick_name_dict = {}
    answer = []
    result = []
    
    for i in record:
        # print(i.split())
        if i[0] == 'E':
            action, uid, nick_name = i.split()
            nick_name_dict[uid] = nick_name
            answer.append(f'{uid}님이 들어왔습니다.')
            
        elif i[0] == 'C':
            action, uid, nick_name = i.split()
            nick_name_dict[uid] = nick_name
            
        elif i[0] == 'L':
            action, uid = i.split()
            if uid in nick_name_dict.keys():
                answer.append(f'{uid}님이 나갔습니다.')
    
    if answer:
        for j in answer:
            uid, _ = j.split()
            uid = uid[:-2]
            # print(j)
            result.append(j.replace(uid, nick_name_dict[uid]))
            
    # print(result)
    return result