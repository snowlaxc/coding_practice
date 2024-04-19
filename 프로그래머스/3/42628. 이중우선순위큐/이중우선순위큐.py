def solution(operations):
    queue = []
    
    for i in operations:
        if i == "D -1":
            if queue:
                queue.remove(min(queue))
        elif i == "D 1":
            if queue:
                queue.remove(max(queue))
        else:
            _, num = i.split(" ")
            num = int(num)
            queue.append(num)

    # print(queue)
    
    return [max(queue), min(queue)] if queue else [0, 0]