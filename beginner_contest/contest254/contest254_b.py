N = int(input())
A = []
for i in range(N):
    A.append([1] * (i + 1))

for i in range(1, N):
    for j in range(1, N):
        if i < j:
            continue
        # j=0 または j=i の時、a=1
        if j == i:
            A[i][j] = 1
        else:
            A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

for a in A:
    res = [str(aa) for aa in a]
    print(" ".join(res))
