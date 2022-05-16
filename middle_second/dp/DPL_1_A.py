# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
n, m = map(int, input().split())
C = list(map(int, input().split()))

CC = []
for _ in range(m):
    CC.append([50001] * (n + 1))


# 初期値を設定
sc = C[0]
for i in range(n + 1):
    if i % sc == 0:
        CC[0][i] = i // sc

for i in range(1, m):
    for j in range(n + 1):
        CC[i][j] = min(CC[i][j], CC[i - 1][j])
        if j - C[i] >= 0:
            CC[i][j] = min(CC[i][j], CC[i - 1][j - C[i]] + 1, CC[i][j - C[i]] + 1)

r = 50001
for cc in CC:
    r = min(r, cc[n])

print(r)
