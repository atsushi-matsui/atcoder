# # https://atcoder.jp/contests/abc246/tasks/abc246_c
N, K, X = map(int, input().split())
A = list(map(int, input().split()))
left = list()

for a in A:
    if K == 0:
        left.append(a)
    else:
        z = a // X
        if z <= K:
            left.append(a % X)
            K -= z
        else:
            left.append(a - (K * X))
            K = 0

if K == 0:
    print(sum(left))
else:
    left.sort(reverse=True)
    left2 = list()
    for a in left:
        if K == 0:
            left2.append(a)
        else:
            K -= 1
    print(sum(left2))


# 8 3 10 5 13
# 1 3 10 5 13
# 1 3 3 5 13
# 1 3 3 5 6
# 1 3 3 5 0
