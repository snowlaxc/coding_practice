def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(list(char for char in new_id if char.isalnum() or char in ['-', '_', '.']))
    # print(new_id)
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # print(new_id)
    
    if new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    # print(new_id)

    return new_id