A = list(map(int, input().split()))

res = A[0]
for _ in range(2):
    res = A[res]

print(res)