#https://atcoder.jp/contests/abc241/tasks/abc241_b

N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_ok = True
for i in range(M):
    try:
        A.remove(B[i])
    except ValueError:
        is_ok = False

if is_ok:
    print("Yes")
else:
    print("No")
   