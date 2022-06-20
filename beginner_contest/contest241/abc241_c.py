N = int(input())
S = []
for i in range(N):
    S.append(input())

is_result = False

for i in range(N):
    if is_result:
        break
    for j in range(N):
        a_count = 0
        b_count = 0
        c_count = 0
        d_count = 0
        for ii in range(6):
            if j+ii < N:
                if S[i][j+ii] == "#":
                    a_count +=1
            else:
                a_count = 0
            if i+ii < N:
                if S[i+ii][j] == "#":
                    b_count +=1
            else:
                b_count = 0
            if i+ii < N and j+ii < N:
                if S[i+ii][j+ii] == "#":
                    c_count +=1
            else:
                c_count = 0
            if i-ii >= 0 and j+ii < N:
                if S[i-ii][j+ii] == "#":
                    d_count +=1
            else:
                d_count = 0
        if a_count >=4 or b_count>= 4 or c_count>=4 or d_count>=4:
            is_result = True
            break

if is_result:
    print("Yes")
else:
    print("No")