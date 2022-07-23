# https://atcoder.jp/contests/abc260/tasks/abc260_a
S = list(input()) 

for s in S:
    if S.count(s) == 1:
        print(s)
        exit()
        
print(-1) 