N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))


for q in range(Q):
    if A[L[q] - 1] == N:
        continue
    if L[q] == K and A[L[q] - 1] < N:
        A[L[q] - 1] += 1
        continue
    c = A[L[q] - 1]
    n = A[L[q]]
    if c + 1 == n:
        continue
    else:
        A[L[q] - 1] = c + 1

ans = [str(a) for a in A]

print(" ".join(ans))
