#https://atcoder.jp/contests/abc114/tasks/abc114_c
import sys
sys.setrecursionlimit(10**9)
N = int(input())

result = 0

def dfs(n, isUsed3, isUsed5, isUsed7):
    global result
    if n > N:
        return
    if isUsed3 and isUsed5 and isUsed7:
        result+=1

    dfs(10*n+3, True, isUsed5, isUsed7)
    dfs(10*n+5, isUsed3, True, isUsed7)
    dfs(10*n+7, isUsed3, isUsed5, True)

dfs(0, False, False, False)
print(result)