# Author: Daniel Soheili
# Date: Jan.8, 2017

from sympy.ntheory import isprime

def findNumberOfVisits(houseNum, elfNum):
    count = 0
    currentHouseNum = houseNum
    while ((currentHouseNum % elfNum == 0) and (currentHouseNum != elfNum)):
        currentHouseNum = currentHouseNum / 2
        count += 1
    # Since this function counts the additional times an elf visits, subtract 1.
    # Otherwise leave it as 1 to avoid multiplication by 0.
    if count > 1: count-=1
    return count

def printDetails(houseNum, givenGifts, totalGifts):
    print "House number", houseNum, "has received at least", givenGifts, "gifts."
    print "[ Actual amount of gifts for house number", houseNum, "=", totalGifts, "]"

def checkTotal(houseNum, totalGifts):
    print "[ Gifts for house number", houseNum, "=", totalGifts, "]"

awaitingInput = True
while (awaitingInput):
    try:
        givenGifts = int(input("Please enter number of gifts: "))
        awaitingInput = False
    except:
        print("Error: Input must be an integer")

loop = True
houseNum = 1
totalGifts = 10
if (givenGifts == totalGifts):
    printDetails(houseNum, givenGifts, totalGifts)
else:
    houseNum = 2
    while (loop):
        if isprime(houseNum):
            totalGifts += (houseNum * 10)
            if (givenGifts <= totalGifts):
                loop = False
                printDetails(houseNum, givenGifts, totalGifts)
            else:
                #checkTotal(houseNum, totalGifts)
                totalGifts = 10
                houseNum += 1
        else:
            # Find which primes houseNum is divisible by and update total
            elfNum = 2
            totalGifts += (houseNum * 10)
            while (elfNum <= houseNum):
                if (houseNum % elfNum == 0):
                    numberOfVisits= findNumberOfVisits(houseNum, elfNum)
                    totalGifts += elfNum * 10 * numberOfVisits
                    elfNum += 1
                else:
                    elfNum += 1
            if (givenGifts <= totalGifts):
                loop = False
                printDetails(houseNum, givenGifts, totalGifts)
            else:
                #checkTotal(houseNum, totalGifts)
                totalGifts = 10
                houseNum += 1
