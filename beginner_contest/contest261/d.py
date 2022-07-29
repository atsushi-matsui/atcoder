N, M = map(int, input().split())
X = list(map(int, input().split()))
X.insert(0,0)
B = [0] * (N+1)
for m in range(M):
    c, y = map(int, input().split())
    B[c] = y
    
# コイントスの回数、カウンタの配列
amount = []
for i in range(N+1):
    amount.append([0]*(N+1)) 

amount[0]
for i in range(1, N+1):
    for j in range(1, N+1):
        # コイントスの回数がカウンタを超えることはない
        if i < j:
            continue
        # 表の場合
        amount[i][j] = max(amount[i][j], amount[i-1][j-1] + X[i] + B[j])
        # 裏の場合
        amount[i][0] = max(amount[i][0], amount[i-1][j-1])
        
        
print(max(amount[-1]))