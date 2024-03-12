dist = int(input())
steps = [5,4,3,2,1]
stepCnt=0
while dist>0:
    for i in steps:
        while dist-i>=0:
            dist=dist-i
            stepCnt+=1

print(stepCnt)