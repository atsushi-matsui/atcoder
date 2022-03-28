# https://atcoder.jp/contests/abc239/tasks/abc239_d

A,B,C,D = list(map(int, input().split()))

def eratosthenes(N):
    table = [True]*N
    table[0]=table[1]=False

    for i in range(2,N):
        if not table[i]:
            continue
        for j in range(i*2,N,i):
            table[j] = False
    
    return table

table = eratosthenes(201)

is_prime=False
for i in range(A,B+1):
    if all(not table[i+j] for j in range(C,D+1)):
        print("Takahashi")
        exit()

print("Aoki")