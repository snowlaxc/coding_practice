num = int(input())

for i in range(1, num + 1):
	time = int(input())
	costs = list(map(int, input().split()))
	costs.reverse()
	
	benefit = 0
	cost_max = 0
	for cost in costs:
		if cost > cost_max:
			cost_max = cost
		else:
			benefit += (cost_max - cost)

	print('#{} {}'.format(i, benefit))