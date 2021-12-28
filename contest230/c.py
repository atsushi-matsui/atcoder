# https://atcoder.jp/contests/abc230/tasks/abc230_c
# ポイント：最大10^18なので全探索すると実行時間が足りない
N, A, B = list(map(int, input().split()))
P, Q, R, S = list(map(int, input().split()))

for i in range(P, Q+1):
    # ans+= みたいにすると毎回変数にメモリを再割り当てするので、実行時間もメモリもオーバーになる。
    # 最後に結合すること
    '''
    ans 
    '''
    ans = []
    for j in range(R, S+1):
        if (i-j-A+B == 0) or (i+j-A-B == 0):
            ans.append('#') 
        else:
            ans.append('.') 
    print("".join(ans))