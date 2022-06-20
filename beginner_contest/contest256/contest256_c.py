B = 1
T = 29

h1, h2, h3, w1, w2, w3 = map(int, input().split())
line1 = []
line2 = []
line3 = []
res = 0
for i1 in range(B, T):
    for i2 in range(B, T):
        for j1 in range(B, T):
            for j2 in range(B, T):
                i3 = h1 - i1 - i2
                j3 = h2 - j1 - j2
                k1 = w1 - i1 - j1
                k2 = w2 - i2 - j2
                k3 = w3 - i3 - j3
                if (
                    h3 == k1 + k2 + k3
                    and B <= i3 < T
                    and B <= j3 < T
                    and B <= k1 < T
                    and B <= k2 < T
                    and B <= k3 < T
                ):
                    res += 1

print(res)
