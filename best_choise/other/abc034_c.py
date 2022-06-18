# https://atcoder.jp/contests/abc034/tasks/abc034_c
"""
検討
1.(H+W-2)!などは大きすぎて計算結果が期待通りではない
2.割り算だと計算途中でmodを取ることができない

方針
1.掛け算だけの式にすることで、各項目でmodをとることができる
2.1を実行するため、フェルマーの小定理を利用する
 aが素数、pがaの倍数出ない場合に、
 a^(-1) ≡ a^(p-2)が成り立つ
 
参考
https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-%E5%89%B2%E3%82%8A%E7%AE%97-a%E2%80%93b
"""
M = 1000000007
MAX = 2 * 10**5
W, H = map(int, input().split())

W -= 1
H -= 1

# 逆元
def inv(n):
    return pow(n, M - 2, M)


fact = [1] * (MAX + 1)
for i in range(MAX):
    # 各階乗のmod(P)を求めておく
    fact[i + 1] = fact[i] * (i + 1) % M
# nCrの組み合わせを求めるのと同義
ans = (fact[W + H] * inv(fact[W]) * inv(fact[H])) % M
print(ans)
