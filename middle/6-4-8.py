#https://atcoder.jp/contests/dp/tasks/dp_g
#計算量:O(N+M)
#NOTICE メモ化しないと実行時間を超過する
import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))
#ノードiの子供
child_node = []
for _ in range(N):
    child_node.append([]*M)
for _ in range(M):
    x, y = list(map(int, input().split()))
    child_node[x-1].append(y-1)

#計算済フラグ（メモ化）
done = [False]*N
#頂点iの有向パス
length = [0]*N

def dfs(i):
    if done[i]:
        return length[i]

    if len(child_node[i]) == 0:
        return length[i]

    for node in child_node[i]:
        length[i] = max(length[i], dfs(node)+1)

    done[i] = True

    return length[i]    

result = []
for i in range(N):
    result.append(dfs(i))

print(max(result))