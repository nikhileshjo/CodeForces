frdCnt,fncHeight = (map(int,input().split()))
friendHeight = list(map(int,input().split()))
bent = [1 for i in friendHeight if (i>fncHeight) ]
width=(frdCnt-len(bent))+(2*len(bent))

print(width)