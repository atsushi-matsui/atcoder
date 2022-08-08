n = int(input())
P = list(map(int, input().split()))

a = n-2
ans = 0
while 1 > 0:
    if a < 0:
        break
    a = P[a] - 2
    ans +=1
    
print(ans)