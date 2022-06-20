N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print("Yes")
    exit()

B = []
for _ in range(K):
    B.append(list())
for i, v in enumerate(A):
    B[i % K].append(v)
for b in B:
    b.sort()
res = [0] * N
for i in range(N):
    res[i] = B[i % K][i // K]

A.sort()
if A == res:
    print("Yes")
else:
    print("No")
