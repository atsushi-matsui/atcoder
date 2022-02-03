#https://atcoder.jp/contests/abc161/tasks/abc161_d
from collections import deque

K = int(input())

#キュー
Q = deque()

#初期設定
for i in range(9):
    Q.append(i+1)
k = 0

#bfs
while len(Q) > 0:
    k += 1
    q = Q.popleft()
    if k == K:
        print(q)
        break
    ones_place = q%10

    left = 0
    center = 0
    right = 0

    if ones_place == 0:
        center = q*10+(ones_place)
        right = q*10+(ones_place+1)
    elif ones_place == 9:
        left = q*10+(ones_place-1)
        center = q*10+(ones_place)
    else:
        left = q*10+(ones_place-1)
        center = q*10+(ones_place)
        right = q*10+(ones_place+1)

    if left != 0:
        Q.append(left)
    if center != 0:
        Q.append(center)
    if right != 0:
        Q.append(right)