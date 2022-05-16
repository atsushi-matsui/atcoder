# https://atcoder.jp/contests/abc026/tasks/abc026_c
import sys
sys.setrecursionlimit(10**6)

N = int(input())
child = []
for i in range(N):
    child.append([])
for i in range(1, N):
    B = int(input())
    child[B-1].append(i)

def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        salary = []
        for c in child[i]:
            salary.append(dfs(c))
        return max(salary)+min(salary)+1

print(dfs(0))