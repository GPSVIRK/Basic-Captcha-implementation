import random as rnd

rnd.seed()
DATA = {"apple":1, "car":0, "banana":1, "pineapple":1, "mango":1, "tire":0, "steering":0, "wheel":0}
#str:key, if key1 == key2 then str1 and str2 are related

def distortWord(word): #would use generator,instead using premade distortions
    return "images/"+word+".png"

def displayWord(word, wordImg): #with tkinter
    print(word)

def distortDisplayWord(word):
    wordImg = distortWord(word)
    displayWord(word, wordImg)

def getWordInputs():#would use tkinter to get the selected buttons
    print("write down the words, comma separated")
    words=input().split(',')
    words = [word.strip() for word in words]
    return words

def validate(mainWord, validWords):#will use tkinter display, button select, submit calls this
    words = getWordInputs()

    for word in words:
        if (DATA[word] != DATA[mainWord]) & (word not in validWords):
            return False

    return True

words = list(DATA.keys())
