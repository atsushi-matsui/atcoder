x1, y1, x2, y2 = list(map(int, input().split()))

is_ok = False

for x in range(x1-3, x1+3):
    for y in range(y1-3, y1+3):
        a = (x1-x)**2+(y1-y)**2
        b = (x2-x)**2+(y2-y)**2

        if a == b == 5:
            is_ok = True
            break
if is_ok:
    print("Yes")
else:
    print("No")