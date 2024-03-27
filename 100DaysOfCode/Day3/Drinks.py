def convert(x):
    return int(x)/100
drinkCnt=int(input())
drinkRatio=list(map(convert,input().split()))

result = (sum(drinkRatio)/drinkCnt)*100
print(result)