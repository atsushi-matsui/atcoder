S = input()
T = 'oxx'*10**5

result = T.__contains__(S)

if result:
    print('Yes')
else:
    print('No')