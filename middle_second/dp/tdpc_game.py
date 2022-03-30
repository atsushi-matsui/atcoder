# https://atcoder.jp/contests/tdpc/tasks/tdpc_game
A, B = list(map(int, input().split()))
a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]

# カードAの残数がi、カードBの残数がj枚の場合のすぬけの価値
value = []
for i in range(A + 1):
    value.append([0] * (B + 1))

for i in range(A + 1):
    for j in range(B + 1):
        # 手番がすぬけの場合
        if (A + B - i - j) % 2 == 0:
            if i > 0 and j > 0:
                value[i][j] = max(
                    value[i - 1][j] + a[A - i], value[i][j - 1] + b[B - j]
                )
            elif i == 0 and j > 0:
                value[0][j] = value[0][j - 1] + b[B - j]
            elif j == 0 and i > 0:
                value[i][0] = value[i - 1][0] + a[A - i]
        # 手番がすめけの場合
        else:
            if i > 0 and j > 0:
                value[i][j] = min(value[i - 1][j], value[i][j - 1])
            elif i == 0 and j > 0:
                value[0][j] = value[0][j - 1]
            elif j == 0 and i > 0:
                value[i][0] = value[i - 1][0]

print(value[A][B])
