import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N = int(lines[0])

    targets = []
    for i in range(1,N+1):
        a, b = list(map(int, lines[i].split()))

        if(a > b):
            targets.append([int(str(b)+str(a)), 0])
        elif(a < b):
            targets.append([int(str(a)+str(b)), 1])
        else:
            targets.append([int(str(a)+str(b)), 2])

    #print(targets)
        
    sorted_targets = sorted(targets)
    #print(sorted_targets)

    #初期値
    t = sorted_targets[0][0]
    count_first = 0
    count_second = 0
    result = 0

    for k, flg in sorted_targets:
        if t == k and flg == 0:
            count_first += 1
        elif t == k and flg == 1:
            count_second += 1
        elif t == k and flg == 2:
            count_first += 0.5
            count_second += 0.5
        else:
            result += int(min(count_first, count_second))
            print(t, count_first, count_second, result)
            if flg == 0:
                count_first = 1
                count_second = 0
            elif flg == 1: 
                count_first = 0
                count_second = 1
            else : 
                count_first = 0.5
                count_second = 0.5
        t = k
    
    if count_first > 1 or count_second > 1:
        result += int(min(count_first, count_second))
    
    print(result)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
