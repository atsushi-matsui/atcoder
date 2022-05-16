# https://atcoder.jp/contests/abc026/tasks/abc026_c
N = int(input())
B = []
# 高橋くんの上司はいない
B.append(0)
for i in range(N - 1):
    B.append(int(input()))

# 社員iの給与
salary = []
for i in range(N):
    salary.append(1)
# 一番位の低い上司
min_boss = max(B) - 1

for i in range(min_boss, -1, -1):
    staff_salary = []
    for j in range(1, N):
        boss = B[j] - 1
        if i == boss:
            staff_salary.append(salary[j])

    if len(staff_salary) > 0:
        salary[i] = max(staff_salary) + min(staff_salary) + 1

print(salary[0])
