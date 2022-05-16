# https://atcoder.jp/contests/abc032/tasks/abc032_c
N, K = map(int, input().split())
S = []
for _ in range(N):
    S.append(int(input()))

r = 1
c = 0
right = 0

for left in range(N):
    if S[left] > K:
        right = left + 1
        continue

    while right < N and r * S[right] <= K:
        r *= S[right]
        right += 1

    if r == 0:
        c = N
        break

    r /= S[left]
    if r <= K:
        c = max(c, (right - left))


print(c)
