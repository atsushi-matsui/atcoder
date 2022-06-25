N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split()))
WS = []
for i in range(N):
    WS.append((W[i], S[i]))
WS.sort()

R = []
for i in range(N):
    R.append(WS[i][1])

ans = S.count(1)
x = ans
for i in range(N):
    w, s = WS[i]

    if s == 0:
        x += 1
    if s == 1:
        x -= 1
    if i < N - 1:
        nw, ns = WS[i + 1]
        if w != nw:
            ans = max(ans, x)
    else:
        ans = max(ans, x)

print(ans)
