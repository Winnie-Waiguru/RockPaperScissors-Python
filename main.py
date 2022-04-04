import random

userWins= 0
computerWins=0

choices = ["rock", "paper", "scissors"]

while True:
    userInput = input("Please pick Rock/Paper/Scissors or q to leave game ").lower()
    if userInput == "q":
        break
        
    if userInput not in choices:
        continue
    
    randomNumber= random.randint(0, 2)
    
    computerPick= choices[randomNumber]
    print("computer picked", computerPick)
    
    if userInput == "rock" and computerPick =="scissors":
        print("You won :)")
        userWins += 1
        
    
    elif userInput == "paper" and computerPick =="rock":
        print("You won :)")
        userWins += 1
    
    
    elif userInput == "scissors" and computerPick =="paper":
        print("You won :)")
        userWins += 1
    
    else: 
        print("You lost :(") 
        computerWins += 1  
    
print("You won", userWins, " points")     
print("Computer", computerWins, " points")    
print("Goodbye.")         