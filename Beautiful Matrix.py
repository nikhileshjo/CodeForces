for i in range(5):
    row = input()
    if "1" in row:
        rowCnt = i+1
        row = list(row.split())
        colCnt = row.index("1")+1
        result = abs(3-rowCnt) + abs(3-colCnt)

print(result)