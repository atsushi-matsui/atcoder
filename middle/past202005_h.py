#https://atcoder.jp/contests/past202005-open/tasks/past202005_h

N, L = list(map(int, input().split()))
X = list(map(int, input().split()))
T1, T2 ,T3 = list(map(int, input().split()))

#ハードルの位置
H = [False]*(L+1)
for x in X:
    H[x] = True

dist_time = [10**10]*(L+1)

#スタート
dist_time[0] = 0

#処理開始
for i in range(0, L+1):
    #行動1
    dist_time[i] = min(dist_time[i], dist_time[i-1]+T1)
    #行動2
    if i >= 2:
        dist_time[i] = min(dist_time[i], dist_time[i-2]+T1+T2)
    #行動3
    if i >= 4:
        dist_time[i] = min(dist_time[i], dist_time[i-4]+T1+T2*3)
    #終点にハードルがあれば加算
    if H[i]:
        dist_time[i] += T3

ans = dist_time[L]

#ピッタリ止まる or はみ出しジャンプ
for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, dist_time[i]+(T1//2)+(T2*(L-i-1/2)))

print(ans)
