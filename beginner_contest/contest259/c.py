S = list(input())
T = list(input())


def create_ans(L):

    count = 1
    ANS = []
    for i in range(len(L) - 1):
        l = L[i]
        r = L[i + 1]
        if l == r:
            count += 1
        else:
            if count == 1:
                ANS.append((l, count))
            if count > 1:
                ANS.append((l, count))
                count = 1

    # 最後の行を処理
    ANS.append((L[-1], count))

    return ANS


SS = create_ans(S)
TT = create_ans(T)

#print(SS)
#print(TT)


def ans(A, B):
    if len(A) != len(B):
        return "No"

    for i in range(len(A)):
        if A[i][0] != B[i][0]:
            return "No"
        if A[i][1] > B[i][1]:
            return "No"
        if A[i][1] == 1 and A[i][1] < B[i][1]:
            return "No"

    return "Yes"


print(ans(SS, TT))
