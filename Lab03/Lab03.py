
import math
import time


def randomMathOperation(number):
        ouput=number*19
        return ouput/19
    
while True:
    try:
        myNumber = int(input("Please enter a number: "))
        break
    
    except ValueError:
        print("Ooops! That was no valide number. Try again....")
            
            
myList =[0,1,2,3,4,5,myNumber]
aList = [6,7,8,9]
zeroList=[0]
combinedList=myList+aList
print("Combined List: ", combinedList)

reversedList= combinedList[::-1]
print("Reversed List: ", reversedList)

slicedList=reversedList[2:5]
print("Sliced List: ",slicedList)

myNumber=slicedList[::-1][0]
print("My number: ", myNumber)


letters=["a","b","c","d","e"]

index=0

for i in letters:
    
    if i=="c":
        letters[index]=myNumber
        myNumberIndex=index
        
    index=index+1
    
myNumberAndQuarter=letters[myNumberIndex]+5

myNumberAndQuarter=math.floor(myNumberAndQuarter)

print(randomMathOperation(myNumberAndQuarter))


