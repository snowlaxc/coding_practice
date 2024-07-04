def solution(routes):
    camera = -99999
    answer = 0
    routes = sorted(routes, key = lambda x:x[1], reverse = False)
    print(routes)
    
    for route in routes:
        src, dst = route
        if camera < src:
            answer += 1
            camera = dst
    
    return answer