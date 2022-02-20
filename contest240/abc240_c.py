#dfsだとTLE
N ,X = list(map(int, input().split()))
ab = []
for i in range(N):
    a, b = list(map(int, input().split()))
    ab.append((a, b))

def dfs(value, node):
    if node < 0:
        if value == 0:
            return True
        else:
            return
    if value < 0:
        return

    a, b = ab[node]
    value1 = value-a
    if dfs(value1, node-1):
        return True
    value2 = value-b
    if dfs(value2, node-1):
        return True

    return False

result = dfs(X, N-1)

if result:
    print("Yes")
else:
    print("No")