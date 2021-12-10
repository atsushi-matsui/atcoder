# https://atcoder.jp/contests/arc050/tasks/arc050_b
R, B = list(map(int, input().split()))
x, y = list(map(int, input().split()))

ng = 0
ok = 10**8

while abs(ok-ng) > 1:
    #　確保できる花束の数
    pipot = (ok+ng)//2
