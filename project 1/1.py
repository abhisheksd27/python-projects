#number guessing game using python


import random
import math

lower=int(input("Enter the lower value : "))
higher = int(input("Enter the highest value : "))

x=random.randint(lower,higher)
y=round(math.log(higher-lower+1,2))

count=0
while count<=y:
    count+=1
    num=int(input("Guess the number :" ))
    if num == x:
        print("Congratulation you guessed it right !!!!!")
        break
    elif num > x:
        print("You guessed wrong try less number")
    else:
        print("You guessed wrong try more than that number")

if count>y:
    print("The correct answer is : ",x)
    print("Better luck next time")