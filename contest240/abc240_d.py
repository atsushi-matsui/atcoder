N = int(input())
a = list(map(int, input().split()))
group = []

result = 0
for ai in a:
    if len(group) > 0:
        index, num = group[len(group)-1]
        if index == ai:
            if num+1 == index:
                group.pop(len(group)-1)
                result -= num
            else:
                group[len(group)-1] = (index, num+1)
                result += 1
        else:
            group.append((ai, 1))
            result += 1
    else:
        group.append((ai, 1))
        result += 1

    print(result)