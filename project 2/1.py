import random

name = input("Enter your name : ")
print("All the best ", name)


words = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]

word = random.choice(words)
print("Guess the character !!")

guesses =""
turns =12

while turns >0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("-")
            failed+=1
    
    if failed==0:
        print("You win")
        
        print("The word is ",word)
        break

    print()
    guess=input("Guess a character ")
    guesses+=guess
    
    
    
    if guess not in word:
        turns-=1
        
        print("Wrong")
        
        print("You have",+ turns , "more guesses")
        
        if turns==0:
            print("You loose")
            
