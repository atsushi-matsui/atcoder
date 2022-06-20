# https://atcoder.jp/contests/abc239/tasks/abc239_e
N, Q = list(map(int, input().split()))
X = list(map(int, input().split()))

nodes = [False]*(N+1)
chlid = []
for i in range(N+1):
    chlid.append([]*(N+1))
A1, B1 = list(map(int, input().split()))
A2, B2 = list(map(int, input().split()))
nodes[A1] = True
nodes[B1] = True
nodes[A2] = True
nodes[B2] = True

if A1 == A2:
    chlid[A1].append(B1)
    chlid[A1].append(B2)
if A1 == B2:
    chlid[A1].append(B1)
    chlid[A1].append(A2)
if B1 == A2:
    chlid[A1].append(A1)
    chlid[A1].append(B2)
if B1 == B2:
    chlid[A1].append(A1)
    chlid[A1].append(A2)

for i in range(2, N-1):
    A, B = list(map(int, input().split()))
    if nodes[A]:
        chlid[A].append(B)
        nodes[B] = True
    elif nodes[B]:
        chlid[B].append(A)
        nodes[A] = True

print(chlid)
result = []

def dfs(node):
    result.append((X[node-1], node))
    if len(chlid[node]) == 0:
        return

    for i in chlid[node]:
        dfs(i)

for i in range(Q):
    V, K = list(map(int, input().split()))
    dfs(V)
    result.sort()
    a, b = result[len(result)-K]
    #print(result)
    print(a)
    result = []

