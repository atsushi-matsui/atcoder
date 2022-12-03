# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
INF = 10**18
V, E = map(int, input().split())
G = [] * V
for i in range(V):
    G.append([INF] * V)
for i in range(V):
    G[i][i] = 0
for _ in range(E):
    s, t, d = map(int, input().split())
    G[s][t] = d

for i in range(V):
    for j in range(V):
        for k in range(V):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(V):
    if i != 0:
        print()
    for j in range(V):
        if G[i][j] == INF:
            print("INF", end="")
        else:
            print(G[i][j], end="")
        if j < V:
            print(" ", end="")
