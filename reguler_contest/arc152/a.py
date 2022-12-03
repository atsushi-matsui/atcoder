# https://atcoder.jp/contests/arc152/tasks/arc152_a

N,L = map(int, input().split())
A = list(map(int, input().split()))

index = N
for a in reversed(A): 
    index -= 1
    if a == 2:
        break
    
       
sum = 0 
for i in range(index):
    if A[i] == 1:
        sum += 2
    if A[i] == 2:
        sum += 3

if L - sum >= 2:
    print("Yes")
else:
    print("No")
