n = int(input())
A = list(map(int, input().split()))



"""
1. 項をlまで選ぶとする
2. i番目の要素を選ぶ
3. 選択ずみの項数はjとする
4. 項の総和の余りをkとする
とすると漸化式が成り立つ。dpは場合の数。
- 項iを選ばない場合
dp[i+1][j][k] += dp[i][j][k]
- 項iを選ぶ場合
dp[i+1][j+1][(k+a[i])%l] += dp[i][j][k]
"""

for l in range(1, n):
    #dp配列を初期化する
    dp = [] * (n+1)
    for i in range(n+1):
        dp.append([]*(n+1))
        for j in range(n+1):
            dp[i].append([0]*(n+1))
            
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(l):
            for k in range(l):
                # 選ばない場合
                dp[i+1][j][k] += dp[i][j][k]
                # 選ぶ場合
                dp[i+1][j+1][(k+A[i]%l)] += dp[i][j][k]
    
ans = 0
for DP in dp[n]:
    ans += DP[0]

print(dp)
print(ans)                       
                