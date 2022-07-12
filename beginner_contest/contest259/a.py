N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    a = T - X * D
    print(a + D * M)
