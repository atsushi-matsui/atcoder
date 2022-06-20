# https://atcoder.jp/contests/abc252/tasks/abc252_c
N = int(input())
S = []
for _ in range(N):
    S.append(input())

# 数字iがj番目に現れる回数
C = []
for _ in range(10):
    C.append([0] * 10)

for i in range(N):
    for j in range(10):
        C[int(S[i][j])][j] += 1

result = [0] * 10

for i in range(10):
    for j in range(10):
        result[i] = max(result[i], j + (C[i][j] - 1) * 10)

print(min(result))
