def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬하여 앞뒤에 있는 번호끼리 비교하도록 함

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


# def solution(phone_book):
#     temp = []
    
#     for i in phone_book:
#         i_len = len(i)
        
#         temp = phone_book.copy()
#         temp.pop(temp.index(i))
        
#         for j in temp:
#             if i == j[:i_len]:
#                 return False
            
#     return True