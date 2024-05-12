import math

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    park_dict = {}
    time_dict = {}
    result_dict = {}
    
    for record in records:
        hour = int(record[:2])
        minute = int(record[3:5])
        tm = hour * 60 + minute
        car_num = record[6:10]
        inout = record[11:]
        
        if inout == 'IN':
            park_dict[car_num] = tm
            
        if inout == 'OUT':
            parking_time = tm - park_dict.pop(car_num)
            time_dict[car_num] = time_dict.get(car_num, 0) + parking_time
    
    
    if park_dict:
        for car_num, tm in park_dict.items():
            parking_time = 23 * 60 + 59 - tm
            time_dict[car_num] = time_dict.get(car_num, 0) + parking_time
            
    for car_num, parking_time in time_dict.items():
        if parking_time <= basic_time:
            result_dict[car_num] = basic_fee
        else:
            result_dict[car_num] = basic_fee + math.ceil((parking_time - basic_time)/unit_time) * unit_fee
            
    # print(result_dict)
    
    results = sorted(result_dict.items(), key = lambda x:x[0], reverse = False)
    # print(result)
    
    answer = []
    
    for i in results:
        _, result = i
        answer.append(result)
        
    return answer