# https://atcoder.jp/contests/abc023/tasks/abc023_d
N = int(input())
H = []
S = []
for i in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

left = 0
right = 10**14 + 10**9 + 1

while abs(right - left) > 1:
    center = (right + left) // 2
    is_ok = True
    times = []
    for n in range(N):
        times.append((center - H[n]) // S[n])
    times.sort()
    for n in range(N):
        if center - H[n] < 0 or n > times[n]:
            is_ok = False
            continue

    if is_ok:
        right = center
    else:
        left = center

print(right)
