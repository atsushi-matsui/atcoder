#https://atcoder.jp/contests/past201912-open/tasks/past201912_h
import math

N = int(input())
C = list(map(int, input().split()))
Q = int(input())

#奇数の最小
uneven_min = 1000000000
#偶数の最小
even_min = 1000000000

for i in range(N):
    if i%2 == 0:
        uneven_min = min(C[i] ,uneven_min)  
    else:
        even_min = min(C[i] ,even_min)  
#奇数の売上枚数
uneven_sell = 0
#偶数の売上枚数
even_sell = 0
#全ての売上枚数（出力）
sell = 0

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 偶数番号
        if query[1]%2 == 0:
            if C[query[1]-1] - even_sell - query[2] >= 0:
                sell += query[2]

                C[query[1]-1] -= query[2]
                even_min = min(even_min, C[query[1]-1])
        # 奇数番号
        elif query[1]%2 == 1:
            if C[query[1]-1] - uneven_sell - query[2] >= 0:
                sell += query[2]

                C[query[1]-1] -= query[2]
                uneven_min = min(uneven_min, C[query[1]-1])         

    elif query[0] == 2:
        if uneven_min - query[1] >= 0:
            sell += math.ceil(N/2)*query[1]

            uneven_min -= query[1] 
            uneven_sell += query[1] 

    elif query[0] == 3:
        if min(uneven_min, even_min) - query[1] >= 0:
            sell += N*query[1]

            even_min -= query[1] 
            uneven_min -= query[1]
            even_sell += query[1] 
            uneven_sell += query[1]

    #print('N=',i,'even_min=',even_min,'uneven_min=',uneven_min,'even_sell=',even_sell,'uneven_sell=',uneven_sell)

print(sell)


