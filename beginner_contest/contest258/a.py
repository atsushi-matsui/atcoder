K = int(input())
h = 21 + K // 60
m = K % 60
print(str(h) + ":" + str(m).zfill(2))
