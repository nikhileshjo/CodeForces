#link to problem statement: https://codeforces.com/problemset/problem/344/A

magCnt=int(input())#number of magnets

magGroups=1#intializing magnet group counts
magPrev=input()#This will be used to compare if the previous mangnet was the same

for poles in range(1,magCnt):
    magPole=input()
    # if the magnets are not arranged with same polarity, they will form another group
    if magPole!=magPrev:
        magGroups+=1
    magPrev=magPole
print(magGroups)

#Failed for time complexity