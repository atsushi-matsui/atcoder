# https://atcoder.jp/contests/abc260/tasks/abc260_c
N, X, Y = map(int, input().split())

"""
def rec(level, is_blue):
    if level == 1:
        if is_blue:
            return 1
        else:
            return 0
    
    if(is_blue):
        return rec(level-1 ,False) + rec(level-1 ,True) * Y
    else:
        return rec(level-1 ,False) + rec(level ,True) * X
    
res = rec(N, False)

print(res)
"""

# レベル iの赤い宝石をもった時に得られるレベル1の青い宝石
red = [0] * N
# レベル iの青い宝石をもった時に得られるレベル1の青い宝石
blue = [0] * N
red[0] = 0
blue[0] = 1


for i in range(1, N):
    blue[i] = red[i-1] + blue[i-1]*Y
    red[i] = red[i-1] + blue[i]*X
    
print(red[N-1])