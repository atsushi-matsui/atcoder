# https://atcoder.jp/contests/arc017/tasks/arc017_3
#　計算量：2^N
#  Nが30-40だったら利用できる半分全列挙のアルゴリズム
import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

N, X = list(map(int, input().split()))
first = []
latter = []
for i in range(N):
    w = int(input())
    if int(N/2) < i:
       first.append(w) 
    else:
       latter.append(w) 

dic = defaultdict(int)
result=0

def dfs_first(i, weight):
    if i < len(first):
        # 選ぶ場合
        dfs_first(i+1, weight+first[i])
        # 選ばない場合
        dfs_first(i+1, weight)
    else:
        dic[weight] += 1

def dfs_latter(i, weight):
    global result
    if i < len(latter):
        # 選ぶ場合
        dfs_latter(i+1, weight+latter[i]) 
        # 選ばない場合
        dfs_latter(i+1, weight)
    else:
        result += dic[X-weight]


dfs_first(0, 0)
dfs_latter(0, 0)

print(result)