num = int(input())

for i in range(1, num + 1):
	li = list(map(int, input().split()))
	print("#{} {}".format(i, round(sum(li)/len(li))))
    