"""
いづれの場合も移動距離は
|A-S|+|A-B|+|G-B| である
S or Gの候補は点A,BのいづれかなのでO(N^3)の総当たりで解いてみる

.A..B..S.......G.......
.A....S.B.....G.......
.......S..A.B..G.......
.......S..A....G.B.....
.......S.......G..A..B.
"""
N = int(input())
AB = []
ST = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
    ST.append(a)
    ST.append(b)

result = 10**18
# NOTICE sとtの候補をa or bとしている
for s in ST:
    for g in ST:
        dist = 0
        for a, b in AB:
            dist += abs(a - s) + abs(a - b) + abs(g - b)
        result = min(result, dist)

print(result)
