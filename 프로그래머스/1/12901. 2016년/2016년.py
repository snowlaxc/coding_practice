import datetime

def solution(a, b):
    answer = datetime.date(2016, a, b)
    answer = answer.weekday()
    
    weekday_dict = {
        '0': 'MON',
        '1': 'TUE', 
        '2': 'WED', 
        '3': 'THU', 
        '4': 'FRI', 
        '5': 'SAT', 
        '6': 'SUN', 
    }
    
    return weekday_dict[str(answer)]