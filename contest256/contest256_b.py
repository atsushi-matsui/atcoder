N = int(input())
A = list(map(int, input().split()))

not_goal = 0
c = 0
for i in range(len(A) - 1, -1, -1):
    c += A[i]
    if c < 4:
        not_goal += 1
    else:
        break

print(len(A) - not_goal)
