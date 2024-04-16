#problem statement

dieRolls=list(map(int,input().split()))
maxVal=max(dieRolls)
if maxVal==1:
    print("1/1")
elif maxVal==2:
    print("5/6")
elif maxVal==3:
    print("2/3")
elif maxVal==4:
    print("1/2")
elif maxVal==5:
    print("1/3")
else:
    print("1/6")