# https://atcoder.jp/contests/arc050/tasks/arc050_b
R, B = list(map(int, input().split()))
x, y = list(map(int, input().split()))

'''
作成する花束：mid
赤の花束：a
青の花束：b

mid = a + b
ax+b <= R
by+a <= B
から
mid <= a+b
'''
def check(mid):
    a = (R-mid)//(x-1)
    b = (B-mid)//(y-1)

    return mid <= a+b
    #return a + b <= mid

ok = 0
ng = 10**18
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)