# https://atcoder.jp/contests/abc246/tasks/abc246_b
# x: A = 1: (a ** 2 + b ** 2) ** 0.5

a, b = map(int, input().split())

print(a / (a**2 + b**2) ** 0.5, b / (a**2 + b**2) ** 0.5)


# x ** 2 + y ** 2 = 1
# y = (b / a) * x
