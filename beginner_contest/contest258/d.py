N, X = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

s = A[0] + B[0]
m = X * B[0] + A[0]

for i in range(1, N):
    if i >= X:
        break
    s += A[i] + B[i]
    if m > B[i]:
        m = min(m, (X - i - 1) * B[i] + s)

print(m)
