#https://atcoder.jp/contests/abc226/tasks/abc226_c
import sys
sys.setrecursionlimit(10**6)

N = int(input())
done = [False] * N
line = []
for _ in range(N):
    line.append(list(map(int, input().split())))

def dfs(i):
    if done[i-1]:
        return 0
        
    done[i-1] = True

    t = line[i-1][0]
    k = line[i-1][1]
    
    if(k == 0):
        return t
       
    result = t
    for j in range(2 ,2+k):
        result += dfs(line[i-1][j])

    return result

print(dfs(N))