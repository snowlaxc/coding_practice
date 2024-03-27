def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]    # 행, 열이 반대로 주어지는 문제이므로

    dp = []
    for i in range(n + 1):    # 한줄씩 추가하는 이유는 좌, 윗 칸의 값을 합하므로
        dp.append([0]*(m + 1))
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1)and(j == 1):    # 시작점
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return(dp[n][m])