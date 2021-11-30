# https://atcoder.jp/contests/abc026/tasks/abc026_c
import sys
sys.setrecursionlimit(10**5)

N = int(input())

#社員番号iの子供child[]
child = []
for _ in range(N):
    child.append([])
for i in range(N-1):
    boss = int(input())
    child[boss-1].append(i+1)

def dfs(i):
    if len(child[i]) > 0:
        child_salary = []
        for j in child[i]:
           child_salary.append(dfs(j))
        if len(child_salary) == 1:
            return child_salary[0]*2+1
        if len(child_salary) > 1:
            return max(child_salary)+min(child_salary)+1
    else:
        return 1

print(dfs(0))