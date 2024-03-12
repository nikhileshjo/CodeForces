word=input()
lowerCnt=0
for i in word:
    if i.islower():
        lowerCnt+=1
if lowerCnt>=(len(word)/2):
    print(word.lower())
else:
    print(word.upper())