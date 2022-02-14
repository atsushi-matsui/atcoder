# https://atcoder.jp/contests/past202005-open/tasks/past202005_h
N, L = list(map(int, input().split()))
xn = list(map(int, input().split()))
#ハードルのあり/なし
hurdle = [False]*(L+1)
for x in xn:
   hurdle[x] = True
T1, T2, T3 = list(map(int, input().split()))
#座標iまでの最短時間
dist=[10**18]*(L+1)

#初期化
dist[0] = 0

#DPで解いていく
for i in range(1, L+1):
    #行動1
    pattern1 = dist[i-1] + T1
    if hurdle[i-1]:
        pattern1 += T3 
    #行動2
    pattern2 = 10**18
    if i >= 2 :
        pattern2 = dist[i-2] + T1 + T2
        if hurdle[i-2]:
            pattern2 += T3 
    #行動3
    pattern3 = 10**18
    if i >= 4:
        pattern3 = dist[i-4] + T1 + T2*3
        if hurdle[i-4]:
            pattern3 += T3
    
    dist[i] = min(pattern1, pattern2, pattern3)

# L-3位置から
if hurdle[L-3]:
    dist[L] = min(dist[L] ,dist[L-3]+T1//2+T2*5//2+T3) 
else:
    dist[L] = min(dist[L] ,dist[L-3]+T1//2+T2*5//2)
# L-2位置から
if hurdle[L-2]:
    dist[L] = min(dist[L] ,dist[L-2]+T1//2+T2*3//2+T3) 
else:
    dist[L] = min(dist[L] ,dist[L-2]+T1//2+T2*3//2) 
# L-1位置から
if hurdle[L-1]:
    dist[L] = min(dist[L], dist[L-1]+T1//2+T2//2+T3) 
else:
    dist[L] = min(dist[L], dist[L-1]+T1//2+T2//2)

print(dist[L])
