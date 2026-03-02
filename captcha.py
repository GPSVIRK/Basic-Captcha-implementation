import random as rnd

rnd.seed()
DATA = {"apple":1, "car":0, "banana":1, "pineapple":1, "mango":1, "tire":0, "steering":0, "wheel":0}
#str:key, if key1 == key2 then str1 and str2 are related

def distortWord(word): #would use generator,instead using premade distortions
    return "images/"+word+".png"

def displayWord(word): #with tkinter
    print(word)

def distortDisplayWord(word):
    word = distortWord(word)
    displayWord(word)

for word in DATA:
    print(word)
    distortDisplayWord(word)
