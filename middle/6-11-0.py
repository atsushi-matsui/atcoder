import heapq

N, M = list(map(int, input().split()))
# 頂点i（添字）から頂点j（配列の値）までの重さ（配列の値）
G = []
marked = [False]*N

marked_count = 0

#頂点0をスタートにする
marked[0] = True
marked_count = 1

Q = []

for j, c in G[0]:
    heapq.heappush(Q, (j, c))

# 最小全域木の重み合計
sum = 0

while N > marked_count:
    ci, i = heapq.heappop()

    if marked[i]:
        continue
    
    marked[i] = True
    marked_count += 1

    sum += ci

    # 新しくマークした頂点からの候補を選ぶ
    for (j, cj)  in G[i]:
        if marked[j]:
            continue
        heapq.heappush(Q, (cj, j))

print(sum)
    
    