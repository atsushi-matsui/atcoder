from scipy.special import comb

N = int(input())
A = list(map(int, input().split()))


ok_1 = 0
ok_2 = 0
for i, a in enumerate(A):
    if a == (i+1):
        ok_1 +=1
    else:
        if A[a-1] == (i+1):
            ok_2 +=1
        
    
res = int(comb(ok_1, 2) + ok_2//2)

print(res)