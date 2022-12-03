"""
1≤H2≤H1≤10
1≤W2≤W1≤10
より、全探索で間に合うのでbit全探索する
"""

H1, W1 = map(int, input().split())
A = []
for _ in range(H1):
    A.append(list(map(int, input().split())))
    
H2, W2 = map(int, input().split())
B = []
for _ in range(H2):
    B.append(list(map(int, input().split())))

ans = [[0 for _ in range(W2)] for _ in range(H2)]

for i in range(2 ** H1):
    if H2 != bin(i).count("1"):
        continue
    rows = [j for j in range(H1) if ((i >> j) & 1)]
    print(rows)
             
    for ii in range(2 ** W1):
        if W2 != bin(ii).count("1"):
            continue
        columns = [jj for jj in range(W1) if ((ii >> jj) & 1)]
        print(columns)
        
        for ri, rv in enumerate(rows):
            for ci, cv in enumerate(columns):
                ans[ri][ci] = A[rv][cv]
        if ans == B:
            print("Yes")
            exit()
            

print("No")
