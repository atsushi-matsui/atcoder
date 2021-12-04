# https://atcoder.jp/contests/past201912-open/tasks/past201912_i

N, M = list(map(int, input().split()))
S = [0]
C = [0]
for _ in  range(M):
    s, c = input().split()
    s = s.replace("Y", "1").replace("N", "0")
    S.append(int(s, 2))
    C.append(int(c))

# 部品セットをi個購入してj種類の商品がある場合の金額amount[i][j]
amount = []
for _ in range(M+1):
    amount.append([10**100]*(1<<N))

# 初期化
amount[0][0] = 0

# メイン処理
# 計算量：M*(2^N)
# NOTICE Nが1未満の制約があるので成り立つ
for i in range(1, M+1):
    for j in range(1<<N): 
        # セットiを購入しない場合
        amount[i][j] = min(amount[i][j], amount[i-1][j])
        # セットiを購入する場合
        amount[i][j|S[i]] = min(amount[i][j|S[i]], C[i]+amount[i-1][j])

result = amount[M][(1<<N)-1]
if result != 10**100:
    print(result)
else:
    print(-1)
