inputCnt = int(input())
x = 0
for _ in range(inputCnt):
    operation = input()
    if "+" in operation:
        x+=1
    else:
        x-=1
print(x)