N,X,Y,Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SCORE = []
for i in range(N):
    SCORE.append([i +1, A[i],B[i], A[i]+B[i]])

ans = []

A = sorted(SCORE, key=lambda x: x[1], reverse=True)
for a in A[:X]:
    ans.append(a[0])

tmp_B = A[X:]
tmp_B.sort()
B = sorted(tmp_B, key=lambda x: x[2], reverse=True)
for b in B[:Y]:
    ans.append(b[0])


tmp_C = B[Y:]
tmp_C.sort()
C = sorted(tmp_C, key=lambda x: x[3], reverse=True)
for c in C[:Z]:
    ans.append(c[0])

ans.sort()
for a in ans:
    print(a)