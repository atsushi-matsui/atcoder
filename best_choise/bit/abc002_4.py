# https://atcoder.jp/contests/abc002/tasks/abc002_4
# 計算量:O(2^N * N)
N, M = map(int, input().split())
XY = []
for _ in range(M):
    XY.append(list(map(int, input().split())))

K = []
for i in range(N):
    K.append(1 << i)
for xy in XY:
    x = xy[0] - 1
    y = xy[1] - 1
    # お互いが面識があれば追加する
    K[x] = K[x] | 1 << y
    K[y] = K[y] | 1 << x

result = 0
for i in range(1 << N):
    # 組み合わせ分だけを確認対象にする
    r = i
    for j in range(N):
        if (i >> j) & 1:
            # お互いに認識があるのかを論理積を取って確認する
            r = r & K[j]
    c = 0
    for j in range(N):
        if (r >> j) & 1:
            # bitが1の社員同士が認識があるので数える
            c += 1
    result = max(result, c)

print(result)
