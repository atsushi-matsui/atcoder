# https://atcoder.jp/contests/typical90/tasks/typical90_ah

"""
example

5 2
1 2 4 4 5

1
1 2
1 2 4
1 2 4 4
1 2 4 4 5
2
2 4
2 4 4
2 4 4 5
4
4 4
4 4 5
4
4 5
5

長さnの数列の部分列の数 = n(n+1)//2
n = 100000
"""

from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

right = 0
result = 0
target = Counter()
for left in range(N):

    # index error にならないか検査する。最左辺で評価
    # NOTICE right < N
    while right < N and len(target) <= K:
        target[A[right]] += 1
        right += 1
        # result = max(result, abs(right - left))

    # NOTICE 最右辺まで到達した場合
    if right == N and len(target) <= K:
        result = max(result, abs(right - left))
    elif len(target) <= K:
        result = max(result, abs(right - left - 1))

    if left == right:
        right = left + 1
    # valueが0になったら要素を削除
    target[A[left]] -= 1
    if target[A[left]] == 0:
        del target[A[left]]

print(result)


"""
 Sample
"""
# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
# 尺取法

"""
right = 0
result = 0
for left in range(N):
    while right < N and "満たさないと条件":
        target[A[right]] += 1  # rightを伸ばす処理
        right += 1

    # 何かしらresult等を更新

    # 追いついたとき用の処理
    if left == right:
        right = left + 1
    # lを削る処理を入れる
    else:
        target[A[left]] -= 1
"""
