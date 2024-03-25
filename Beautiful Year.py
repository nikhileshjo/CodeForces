givenYear = int(input())
tmpYear=givenYear+1
while True:
    tmpSet = set(str(tmpYear))
    tmpList = str(tmpYear)
    if len(tmpSet)==len(tmpList):
        break
    tmpYear+=1
print(tmpYear)