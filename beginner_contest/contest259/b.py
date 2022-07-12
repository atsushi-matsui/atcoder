import math

a, b, d = map(int, input().split())

sin = math.sin(math.radians(d))
cos = math.cos(math.radians(d))

x = a * cos - b * sin
y = a * sin + b * cos

print(x)
print(y)
