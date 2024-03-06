participants, pos = map(int,input().split())
points = list(map(int,input().split()))

advanced = 0
for i in points:
    if i>=points[pos-1] and i>0:
        advanced+=1
    else:
        break
print(advanced)