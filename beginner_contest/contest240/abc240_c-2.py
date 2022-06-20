N, X = list(map(int, input().split()))
dist = []
for i in range(N+1):
    dist.append([False]*10001)

dist[0][0] = True

for i in range(1, N+1):
    a, b = list(map(int, input().split()))
    for j in range(10001):
        if dist[i-1][j]:
            dist[i][j+a] = True
            dist[i][j+b] = True

if(dist[N][X]):
    print("Yes")
else:
    print("No")