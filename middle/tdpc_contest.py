# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

N = int(input())
ps = list(map(int, input().split()))

sum_p = sum(ps)

exist = []
for _ in range(N):
    exist.append([False]*(sum_p+1))

exist[0][0] = True

for n in range(N):
    for p in range(sum_p+1):
        if n == 0 and p == ps[0]:
           exist[n][p] = True
        #i問目を解かない場合
        if n > 0 and exist[n-1][p]:
            exist[n][p] = True
        #i問目を解いた場合
        if n > 0 and p-ps[n] >=0 and exist[n-1][p-ps[n]]:
            exist[n][p] = True
        #print(n, p ,exist[n][p])

result_count = 0
for p in range(sum_p+1):
    if exist[N-1][p]:
        result_count += 1
    
print(result_count)