N, X = map(int, input().split())
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alpha[(X - 1) // N])
