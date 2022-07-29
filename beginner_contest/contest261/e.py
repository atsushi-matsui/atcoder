# https://atcoder.jp/contests/abc261/tasks/abc261_e
"""
論理演算の累積和を各bit列で求める。
O(N)

関連問題
https://atcoder.jp/contests/abc147/tasks/abc147_d
"""
BIT = 30
n, c = map(int, input().split())
bit = [[0,1] for _ in range(BIT)]
    
for i in range(n):
    t, a = map(int, input().split())
    
    for j in range(BIT):
        b = a >> j & 1
        
        if t == 1:
            bit[j][0] &= b
            bit[j][1] &= b
        elif t == 2:
            bit[j][0] |= b
            bit[j][1] |= b
        elif t == 3:
            bit[j][0] ^= b
            bit[j][1] ^= b
    
    
    cc = 0
 
    for j in range(BIT):
        if bit[j][c>>j &1]:
            cc += 1 << j
    c = cc
    print(c)
