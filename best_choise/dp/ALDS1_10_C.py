# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
# FIXME TLEになるので改良が必要
"""
入力例1

  a b c b d a b 
b 0 1 1 1 1 1 1
d 0 1 1 1 2 2 2
c 0 1 2 2 2 2 2
a 1 1 2 2 2 3 3
b 1 2 2 3 3 3 4
a 1 2 2 3 3 4 4

入力例2
  b b b
b 1 1 1
b 1 2 2
b 1 2 3

i行、j列とすると
・i != jの場合は上か左の最大値をとる
X[i][j] = max(X[i-1][j], X[i][j-1])
・i == jの場合は左斜め上 + 1
X[i][j] = X[i-1][j-1] + 1
"""

N = int(input())

result = []
for _ in range(N):
    X = list(input())
    Y = list(input())

    XY = []
    for _ in range(len(X)):
        XY.append([0] * len(Y))

    for i in range(len(X)):
        if Y[0] == X[i]:
            XY[i][0] = 1
        else:
            if i != 0:
                XY[i][0] = XY[i - 1][0]
            else:
                XY[i][0] = 0
    for j in range(len(Y)):
        if X[0] == Y[j]:
            XY[0][j] = 1
        else:
            if j != 0:
                XY[0][j] = XY[0][j - 1]
            else:
                XY[0][j] = 0

    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                # これだと入力例2の場合にNGになる
                # XY[i][j] = max(XY[i - 1][j], XY[i][j - 1]) + 1
                XY[i][j] = XY[i - 1][j - 1] + 1
            else:
                # maxはh O（N）かかるので、ifで比較
                # XY[i][j] = max(XY[i - 1][j], XY[i][j - 1])
                if XY[i - 1][j] >= XY[i][j - 1]:
                    XY[i][j] = XY[i - 1][j]
                else:
                    XY[i][j] = XY[i][j - 1]

    result.append(XY[len(X) - 1][len(Y) - 1])

for r in result:
    print(r)
