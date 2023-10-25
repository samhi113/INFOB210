# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:56:41 2023

@author: samhi
"""

numQ1 = 0
i = 2
j = 2
isPrime = False

def getNumQ1():
    global numQ1
    try:
        numQ1 = abs(int(input("What should the highest possible number be?\n")))
    except (ValueError):
        print("\nERROR: Not an integer. Please type a number above 1.")
        getNumQ1()
    print("\n\nAll primes below", numQ1,":")

def evalForPrimes():
    global i, j, isPrime
    for i in range(numQ1):
        for j in range(numQ1):
            if (i < 2):
                i = 2
            
            if (j < 2):
                j = 2
            
            if (i % j == 0 and i > j):
                isPrime = False
                break
            else:
                isPrime = True
        
        if (isPrime):
            print(i)

getNumQ1()
evalForPrimes()






#Question 2

numRows = 1

def getRowsQ2():
    global numRows, valueList
    
    # get the row count
    try:
        numRows = abs(int(input("How many rows in Pascal's Triangle?\n")))
    except:
        print("\nERROR: Not an integer. Please type a number above 1.")
        getRowsQ2()


def makeTriangle():
    for a in range(numRows + 1):
        for b in range(numRows - a):
            print(" ", end="")
        
        c = 1
        for b in range(1, a+1):
            print(c, " ", sep="", end="")
            c = c * (a - b) // b
        print("")
    
getRowsQ2()
makeTriangle()