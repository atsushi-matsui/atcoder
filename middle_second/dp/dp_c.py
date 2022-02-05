# https://atcoder.jp/contests/dp/tasks/dp_c
N = int(input())

# 幸福度
happy = []
for i in range(10**5+1):
    happy.append([0]*3)

#　初期化
a, b, c = map(int, input().split())
happy[0][0] = a
happy[0][1] = b
happy[0][2] = c

for i in range(1, N):
    a, b, c = map(int, input().split())
    # iの活動でaを選んだ場合の幸福度の最大値
    happy[i][0] = a + max(happy[i-1][1], happy[i-1][2])
    # iの活動でbを選んだ場合の幸福度の最大値
    happy[i][1] = b + max(happy[i-1][0], happy[i-1][2])
    # iの活動でcを選んだ場合の幸福度の最大値
    happy[i][2] = c + max(happy[i-1][0], happy[i-1][1])

print(max(happy[N-1]))
