#https://atcoder.jp/contests/abc146/tasks/abc146_c
A, B, X = list(map(int, input().split()))

def calculate_amount_(A, B, N):
    return A*N+B*len(str(N))

ok = 0
ng = 10**9+1

while abs(ok-ng) > 1:
    pipot = (ok+ng)//2
    amount = calculate_amount_(A, B, pipot)

    if amount > X:
        ng = pipot
    else:
        ok = pipot
    #2分探索の確認
    #print(ok, ng, pipot, amount)

if ok != 0:
    print(ok)
else:
    print(0)
    