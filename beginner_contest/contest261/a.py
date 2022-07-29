L1, R1, L2, R2 = map(int, input().split())

R = [False] * 101
B = [False] * 101

for i in range(L1, R1):
    R[i] = True
for i in range(L2, R2):
    B[i] = True
    
res = 0

for i in range(101):
    if R[i] and B[i]:
        res +=1
        
print(res)