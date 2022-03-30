def testaaa(a:str) -> bool:
    """_summary_

    Args:
        a (str): _description_

    Returns:
        bool: _description_
    """
    return True

def _isBingo(bingoCard: str) -> str:
    """_summary_

    Args:
        bingoCard (str): _description_

    Returns:
        str: _description_
    """

    isRowBingo = True
    isLineBingo = True
    isDiagonalingo = True

    for i in range(0, len(bingoCard)):
        if bingoCard[i][0] == False:
            isRowBingo = False
        elif bingoCard[0][i] == False:
            isLineBingo = False
        elif bingoCard[i][i] == False:
            isDiagonalingo = False

        if(not (isRowBingo or isLineBingo or isDiagonalingo)):
            break

    if(isRowBingo or isLineBingo or isDiagonalingo):
        return True


A = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)

    print(A)

# TODO いい感じに記載
bingoCard = [[False, False, False], [
    False, False, False], [False, False, False]]

N = int(input())

for _ in range(0, N):
    b = int(input())

    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                bingoCard[i][j] = True

result = _isBingo(bingoCard)

if result:
    print("Yes")
else:
    print("No")
