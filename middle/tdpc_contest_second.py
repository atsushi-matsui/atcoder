# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
#NOTICE  2^nの計算量で実行時間エラーとなる例

N = int(input())
ps = list(map(int, input().split()))

sum_p = set()

def dfs(i, sum):
    if i >= N:
        return
    #i問目を解かなかった場合
    #if not(sum in sum_p):
    sum_p.add(sum)
    dfs(i+1, sum)

    #i問目を解いた場合
    #if not((sum + ps[i]) in sum_p):
    sum_p.add(sum+ps[i])
    dfs(i+1, sum+ps[i])

dfs(0, 0)

print(len(sum_p))

