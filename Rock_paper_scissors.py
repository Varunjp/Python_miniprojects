import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick+".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        
    elif computer_pick == "scissors" and user_input == "paper":
        print("Computer won!")
        computer_wins += 1 
        
    elif computer_pick == "paper" and user_input == "rock":
        print("Computer won!")
        computer_wins += 1
        
    elif computer_pick == "rock" and user_input == "scissors":
        print("Computer won!")
        computer_wins += 1

    else:
        print("Same selection no points!")
        

if user_wins>computer_wins:
    print("You won!!!! Congrats")
else:
    print("Computer won..Better luck next time")
        

print("You points",user_wins,"times.")
print("Comupter points",computer_wins,"times.")
print("Goodbye!")
