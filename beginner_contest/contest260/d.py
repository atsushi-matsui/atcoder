from collections import deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

targets = []
ans = [-1] * N
for i, p in enumerate(P):
    if K == 1:
        ans[p-1] = i + 1
        continue
    
    if len(targets) == 0:
        q = deque()
        q.append(p)
        targets.append(q)
    else:
        left = -1
        right = len(targets)
        while right - left  > 1:
            middle = (right + left) //2
            t = targets[middle]
            if p <= targets[middle][0]:
                right =  middle
            else:
                left = middle
        if len(targets) == right and targets[right-1][0] < p:
            q = deque()
            q.append(p)
            targets.append(q)
            continue
        # NOTICE: listのinsertで左端に入れようとするとTLE
        targets[right].appendleft(p)
        c = len(targets[right])
        if c == K:
            for t in targets[right]:
               ans[t-1] = i + 1
            targets.pop(right)
            
            

for a in ans:     
    print(a)