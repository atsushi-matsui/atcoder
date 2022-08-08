"""
itertoolsで実装するのではなくこちらの方が問題の意図として適切。
実行時間などはあまり変わらない。
"""

n, m = map(int, input().split())

def dfs(t):
    if len(t) == n:
        print(*t)
        return
    
    for i in range(t[-1] + 1, m+1):
        dfs(t+[i])
        
for i in range(1, m+1):
    dfs([i])