N, Q = map(int, input().split())
S = list(input())

offset = 0

for q in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        offset += b
    else:
        s = -(offset % N)
        print(S[(s + (b - 1))])
