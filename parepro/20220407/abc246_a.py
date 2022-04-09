# https://atcoder.jp/contests/abc246/tasks/abc246_a
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

result_x = 0
result_y = 0
if x1 == x2:
    result_x = x3
elif x2 == x3:
    result_x = x1
elif x3 == x1:
    result_x = x2

if y1 == y2:
    result_y = y3
elif y2 == y3:
    result_y = y1
elif y3 == y1:
    result_y = y2

print(result_x, result_y)

# X = set()
# Y = set()

# for _ in range(3):
#     x, y = map(int, input().split())
#     if x in X:
#         X.discard(x)
#     else:
#         X.add(x)

# print(X[0])

# https://www.mathpython.com/ja/python-set-remove/
