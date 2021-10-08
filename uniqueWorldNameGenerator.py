from tkinter import *
import random
import math
import numpy as np

root = Tk()
root.title('Unique World Name Generator')
root.geometry("600x250")

textGenerated = ""
inputString = ["Sibunerth","Bulugawa","Ugniuq","Punzorth","Riutera","Tourus","Gidihiri","Duvunia","Pholla","Bonkegantu","Oseiruta","Esone","Cithapus","Yawei","Hautune","Lumibos","Strucuhiri","Cherth","Koniuliv","Lalmuiyama","Bucrippe","Ranzurn","Helara","Danov","Chogiter","Phehestea","Streshan 20","Obinia","Dingoihiri","Sobyke","Gomapus","Tinides","Ibos","Nevepra","Thizoria","Thorix","Othawei","Envizuno","Xobbeubos","Tugnarth","Kitryria","Eria","Kaurilia","Chisoter","Thoyeclite","Llides","Bibbeuwei","Pebbuecarro","Henreron","Innone","Vastea","Zuria","Thomizuno","Zopetov","Truna","Ilniawei","Yunkabos","Uphosie","Usara","Setis","Iwei","Duveyama","Subitera","Nadus","Cunvarilia","Ronrulea","Xutrolla","Amapus","Pualara","Xogawa","Striyohines","Tresuvis","Luna","Nankiter","Bichocury","Ogryke","Dallolla","Ubos","Oitov","Cheeter","Llomenope","Niuq","Udragawa","Munvonope","Silurn","Ecriri","Soatov","Meucury","Brichimia","Tretalia","Troth","Hogeatov","Nasiarilia","Xocora","Alvosie","Gacury","Xeuter","Creguter","Phalohiri","Vonoe"]
choice = IntVar()

def cvtInt(value):
    fnum = []
    newnum = ''
    for i in value:
        ii = int(i)
        fnum.append(ii)
    for i in fnum:
        newnum = newnum + str(i)
    new = int(newnum)
    return new

def generator(med, numStandDist, upper, lower):
  mu, sigma = med, numStandDist # mean and standard deviation 
  x = np.random.normal(mu, sigma, 1)
  if x>med:
    x = math.floor(x)
  if x<med:
    x = math.ceil(x)
  if x>upper:
    x = generator(med, numStandDist, upper, lower)
  if x<lower:
    x = generator(med, numStandDist, upper, lower)
  return x

def randName():
  max = len(inputString)
  randIndex = random.randint(0, max)
  word = inputString[randIndex]
  return word

def numOfNames(number):
  names = []
  x=0
  while x < number:
    wordCount = random.randint(2,3)
    wordArray = []
    y=0
    while y < wordCount:
      wordArray.append(randName())
      y=y+1
    if len(wordArray) == 2:
      ffirst = random.randint(2,5)
      fsecond = random.randint(3,5)
      fullWord = (wordArray[0][0:ffirst] + wordArray[1][(len(wordArray[1])-fsecond):len(wordArray[1])])
    elif len(wordArray) == 3:
      ffirst = random.randint(2,5)
      fsecond = random.randint(3,5)
      fthird = random.randint(2,5)
      fullWord = (wordArray[0][0:ffirst] + wordArray[1][0:fsecond] + wordArray[2][(len(wordArray[2])-fthird):len(wordArray[2])])
    names.append(fullWord.capitalize())
    x=x+1
  return names

def displayPlanetNames(choiceInt):
	names = numOfNames(choiceInt)
	generatedTextWidget = Entry(root, width = 250)
	generatedTextWidget.pack()
	generatedTextWidget.insert(0, names)

def triggerGeneration():
	enteredValue = choice.get()
	displayPlanetNames(enteredValue)

clicked = IntVar()
clicked.set("Choose #")
menuChoice = OptionMenu(root, clicked, 1, 5, 10, 15, 20)
menuChoice.pack()

def buttonTrigger():
	choiceInt = clicked.get()
	displayPlanetNames(choiceInt)

promptButtonWidget = Button(root, text = "Generate", command = buttonTrigger, fg = "#000000", bg = "#ffffff")
promptButtonWidget.pack()

root.mainloop()