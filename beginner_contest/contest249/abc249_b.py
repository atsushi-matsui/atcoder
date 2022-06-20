# https://atcoder.jp/contests/abc249/tasks/abc249_b
s = input()

is_ok = True

if s.islower():
    is_ok = False
if s.isupper():
    is_ok = False
if len(list(s)) != len(set(s)):
    is_ok = False

if is_ok:
    print("Yes")
else:
    print("No")
