N = int(input())

S = {}
for _ in range(N):
    s = input()
    c = S.get(s)
    if c is None:
        print(s)
        S[s] = 1
    else:
        print(f"{s}({c})")
        S[s] = c + 1
        