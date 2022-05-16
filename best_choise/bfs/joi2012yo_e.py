# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
# 計算量：O（WH)
from collections import deque

W, H = map(int, input().split())
C = []
C.append([0] * (W + 2))
for _ in range(H):
    c = []
    c.append(0)
    c += list(map(int, input().split()))
    c.append(0)
    C.append(c)
C.append([0] * (W + 2))

# イルミなし0、イルミあり1~6
dist = []
# 訪問ずみであるか
is_visited = []
for _ in range(H + 2):
    dist.append([0] * (W + 2))
    is_visited.append([False] * (W + 2))
# キュー
q = deque()
# 初期値
q.append((0, 0))

while len(q) > 0:
    y, x = q.popleft()

    # 訪問ずみに変更
    if is_visited[y][x]:
        continue
    else:
        is_visited[y][x] = True

    """
    y が奇数の時，座標 (x,y) の正六角形に隣接する南西の正六角形の座標は (x,y+1) である．
    y が偶数の時，座標 (x,y) の正六角形に隣接する南東の正六角形の座標は (x,y+1) である．
    """
    if y % 2 == 1:
        ren = [
            (y - 1, x),
            (y, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
            (y, x + 1),
            (y - 1, x + 1),
        ]
    else:
        ren = [
            (y - 1, x - 1),
            (y, x - 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y, x + 1),
            (y - 1, x),
        ]

    for y2, x2 in ren:
        # 範囲外でないか
        if not (0 <= y2 <= H + 1 and 0 <= x2 <= W + 1):
            continue

        if C[y][x] + C[y2][x2] == 1:
            if not is_visited[y2][x2]:
                dist[y][x] += 1

        # 建物でない、かつ未訪問なら追加
        if C[y2][x2] == 0 and not is_visited[y2][x2]:
            q.append((y2, x2))

result = 0
for d in dist:
    result += sum(d)
print(result)
