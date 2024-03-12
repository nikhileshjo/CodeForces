inNum = input()
sevens = inNum.count("7")
fours = inNum.count("4")
totalLucky=sevens+fours
if totalLucky==7 or totalLucky==4:
    print("YES")
else:
    print("NO")