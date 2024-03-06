def word_abbrivatior(word):
    abbLength=str(len(word)-2)
    result = word[0]+abbLength+word[-1]
    return result

inputCnt = int(input())
for i in range(inputCnt):
    inputWord = input()
    if len(inputWord) > 10:
        print(word_abbrivatior(inputWord))
    else:
        print(inputWord)
