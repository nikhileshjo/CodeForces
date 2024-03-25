# link to problem: https://codeforces.com/problemset/problem/467/A

#number of rooms
roomCnt=int(input())

#counting available rooms
availRooms=0

for room in range(roomCnt):
    ppl,capacity = map(int,input().split())
    #increment availRooms by one if the available space if 2 or more
    if capacity-ppl>=2:
        availRooms+=1
print(availRooms)