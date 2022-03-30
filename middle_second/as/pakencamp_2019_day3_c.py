# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
N, M = list(map(int, input().split()))
A = [] * M
for i in range(N):
    A.append(list(map(int, input().split())))

result = 0
for i in range(M):
    for ii in range(i, M):
        pass
        score = 0
        for j in range(N):
            score += max(A[j][i], A[j][ii])
        result = max(result, score)

print(result)
