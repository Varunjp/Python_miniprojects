name = input("Enter your name: ")
print("Welcome",name,"to the adventure point!!")

answer = input("You are at a dirt road, which have came to an end. You can go left or right (left/right)? : ").lower()

if answer == "left":
    answer = input("There is a river infront. Would you like to swim or walk across river?(swim/walk): ").lower()
    if answer == "swim":
        print("There was a alligator in river and you got bite. You lose...")
    elif answer == "walk":
        print("You have got lost in jungle and ran out of energy. You lose..")
    else:
        print("Wrong decision. You loss")

elif answer == "right":
    answer = input("There is a bridge which looks wobbely and a rocky path on edge of riverfall. Choose the path(bridge/rocky path)? ").lower()
    if answer == "bridge":
        print("The bridge seems too wobbly. Ahhh....wind shit the ropes broke. You fell from bridge. Lost the game..")
    elif answer == "rocky path":
        answer = input("Congrats..!! You have crossed river. Now you could see a light far ahead. Do you wish to go near light(yes/no)? ").lower()

        if answer == "yes":
            print("You found the way to life. Happy journy :) ....")
        else:
            print("Got lost in darkness. Find the way again from starting")

    else:
        print("Wrong choice lost the game.")    

else:
    print("You choose wrong direction. You lose...")
