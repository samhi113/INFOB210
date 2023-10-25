# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:56:52 2023

@author: samhi
"""
import math

lcmORgcf = ""
isLCM = False
firstNumber = 0
secondNumber = 0

def getLcmORgcf():
    global isLCM, lcmORgcf
    try:
        lcmORgcf = input("LCM or GCF?\n")
        
        if (lcmORgcf == "lcm" or lcmORgcf == "LCM" or lcmORgcf[0] == "l" or lcmORgcf[0] == "L"):
            isLCM = True
            
        elif (lcmORgcf == "gcf" or lcmORgcf == "GCF" or lcmORgcf[0] == "g" or lcmORgcf[0] == "G"):
            isLCM = False
            
        else:
            print("ERROR: could not determine LCM or GCF. Retrying process.")
            getLcmORgcf()
        
    except:
        print("ERROR: Didn't execute getLcmORgcf correctly.")

def getNumbers():
    global firstNumber, secondNumber
    try:
        firstNumber = int(input("What is your first number?\n"))
        secondNumber = int(input("What is your second number?\n"))
    except (ValueError):
        print("ERROR: Number couldn't be processed. Try again!")
        getNumbers()

def evalNumbers():
    global firstNumber, secondNumber
    
    #Make sure firstNum > secondNum
    if (firstNumber < secondNumber):
        oldNum = secondNumber + 1 - 1
        secondNumber = firstNumber + 1 - 1
        firstNumber = oldNum + 1 - 1
    
    #Calculate LCM
    if (isLCM):
        divisor = int(secondNumber)
        remainder = firstNumber % secondNumber
        
        #don't crucify me, this is euclid's algorithm
        while (remainder != 0):
            oldRem = remainder + 1 - 1
            remainder = divisor % remainder
            divisor = divisor // oldRem
        
        finalNum = (firstNumber * secondNumber) / divisor
    
    #GCF Time
    else:
        highestPossibleNum = round(math.sqrt(firstNumber))
        finalNum = 1
        
        #but why not the euclidean algorithm? Well, I took one look and said nuh uh. nope. miss me with that.
        while(highestPossibleNum != 1 and finalNum == 1):
            if (firstNumber // highestPossibleNum == firstNumber / highestPossibleNum and secondNumber // highestPossibleNum == secondNumber / highestPossibleNum):
                finalNum = firstNumber // highestPossibleNum
            else:
                highestPossibleNum -= 1
    
    #Final Output
    print("The answer is: ", finalNum)

getNumbers()
getLcmORgcf()
evalNumbers()
print("\n\n")


















#Question 2 baybeeeeee
passageNum = 1
desiredLetter = ""
passageText = ""
letterCount = 0

#passages for a dolla, right here. whatcha want?
def selectPassage():
    global passageNum
    
    #store passageNum as an int
    try:
        passageNum = int(input("Select a passage: (just type the number)\n1) The Raven, paragraph 7, by Edgar Allen Poe\n2) Fire and Ice by Robert Frost\n3) Awaking in New York by Maya Angelou\n4) I'm thankful that my life doth not decieve by Henry David Thoreau\n5) Your own text!\n\n"))
    
    #but if it isn't, redo the process
    except (ValueError or passageNum > 5):
        print("ERROR: BAD_PARSE_SELECT_PASSAGE. Retrying process.")
        selectPassage()

#anything you lookin for?
def pickLetterToSearch():
    global desiredLetter
    desiredLetter = input("What letter should I look for?\n")[0].lower()
    
#actual work from the computer
def findLettersInPassage():
    global passageText, letterCount
    
    #grab text to search
    if (passageNum == 1):
        passageText = "open here i flung the shutter, when, with many a flirt and flutter, in there stepped a stately raven of the saintly days of yore; not the least obeisance made he; not a minute stopped or stayed he; but, with mien of lord or lady, perched above my chamber door— perched upon a bust of pallas just above my chamber door— perched, and sat, and nothing more."
        
    elif (passageNum == 2):
        passageText = "some say the world will end in fire, some say in ice. from what i’ve tasted of desire i hold with those who favor fire. but if it had to perish twice, i think i know enough of hate to say that for destruction ice is also great and would suffice."
        
    elif (passageNum == 3):
        passageText = "curtains forcing their will against the wind, children sleep, exchanging dreams with seraphim. the city drags itself awake on subway straps; and i, an alarm, awake as a rumor of war, lie stretching into dawn, unasked and unheeded."
        
    elif (passageNum == 4):
        passageText = "i’m thankful that my life doth not deceive itself with a low loftiness, half height, and think it soars when still it dip its way beneath the clouds on noiseless pinion like the crow or owl, but it doth know the full extent of all its trivialness, compared with the splendid heights above. see how it waits to watch the mail come in while ’hind its back the sun goes out perchance. and yet their lumbering cart brings me no word, not one scrawled leaf such as my neighbors get to cheer them with the slight events forsooth, faint ups and downs of their far distant friends— and now ’tis passed. what next? see the long train of teams wreathed in dust, their atmosphere; shall i attend until the last is passed? else why these ears that hear the leader’s bells or eyes that link me in procession? but hark! the drowsy day has done its task, far in yon hazy field where stands a barn, unanxious hens improve the sultry hour and with contented voice now brag their deed— a new laid egg—Now let the day decline— they’ll lay another by tomorrow’s sun."
    
    else:
        passageText = input("What is your text?")
    
    #search text for letters
    #probably takes enough power to kill a Windows ME computer, oops
    n=0
    try:
        while (passageText[n] != ""):
            if (passageText[n] == desiredLetter):
                letterCount += 1
            n+=1
    
    #If at end of passage, then
    except (IndexError):
        print("Found ", letterCount, " instances of ", desiredLetter)

selectPassage()
pickLetterToSearch()
findLettersInPassage()