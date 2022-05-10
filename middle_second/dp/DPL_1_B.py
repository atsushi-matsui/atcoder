# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja
"""
価値が vi 重さが wiの品物をi個まで選んだ時の価値の合計求めていく。
その際同じ重さであれば価値が高い品物の組み合わせだけを残していく。

品物iまでを見た時の重さjの価値
V[i][j]
for 
    for 
        (iまで選んだの品物の価値) = (今選んだ品物の価値)+(i-1までの品物の価値) or (今選んだ品物の価値)
"""
N, W = map(int, input().split())
goods = []
for _ in range(N):
    goods.append(list(map(int, input().split())))

V = []
for _ in range(100):
    V.append([0] * (W + 1))

# 初期値を設定
V[0][goods[0][1]] = goods[0][0]
# 処理開始
for i in range(1, N):
    v, w = goods[i]
    for j in range(W + 1):
        # 品物を選ばない場合
        V[i][j] = max(V[i][j], V[i - 1][j])
        # 品物を選ぶ場合
        if j >= w:
            V[i][j] = max(V[i][j], V[i - 1][j - w] + v)

print(max(V[N - 1]))
