gameCnt = int(input())
gameRes = input()
AntonWonCnt = gameRes.count("A")
if AntonWonCnt>(gameCnt/2):
    print("Anton")
elif AntonWonCnt==(gameCnt/2):
    print("Friendship")
else:
    print("Danik")