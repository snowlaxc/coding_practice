num = int(input())

for i in range(1, num+1):
	N, K = map(int, input().split())
	pocket = sorted(list(map(int, input().split())), reverse = False)

	# 정렬시 순서대로 K개 선택하면 됨
	answer = float('inf')
	for j in range(N - K + 1):
		diff = pocket[j + K - 1] - pocket[j]
		answer = min(diff, answer)

	print('#{} {}'.format(i, answer))