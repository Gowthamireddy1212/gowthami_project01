print("Welcome to the Treasure Island")
start = input("You are ready to hunt the treasure, Enter 'Yes' or 'No': ").lower()

if start != "yes":
    print("Maybe next time. Game Over.")
else:
    print("You'll face three decision points, and your choices will decide your fate.")
    choice1 = input("You're at the fork of the road. Choose 'left' or 'right': ").lower()

    if choice1 != "left":
        print("Oops! You fell into a hole. Game Over.")
    else:
        print("Good choice, This is the road that leads to the treasure lake!")
        choice2 = input("You are at the Lake, Decide whether you wanna 'swim' or 'wait': ").lower()

        if choice2 != "wait":
            print("Attacked by hungry trout. Game Over.")
        else:
            print("Thanks for the patience, You have found a boat renting area nearby.")
            print("Bravo, You have made this far. You have given 3 doors, make the choice 'red', 'yellow', or 'blue'.")
            choice3 = input("Which door do you choose? ").lower()

            if choice3 == "red":
                print("Burned by fire. Game Over.")
            elif choice3 == "blue":
                print("Eaten by beasts. Game Over.")
            elif choice3 == "yellow":
                print("🎉 Congrats Adventurer, You have found the treasure! A room full of expensive stones 💎 and gold 🪙")
            else:
                print("Invalid choice. Game Over.")
