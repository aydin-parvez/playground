print("You are in a dark room in a mysterious castle.")
print("In front of you there are 3 doors.You must choose one.")
playerchoice=input("Choose 1,2 or 3...")
if playerchoice=="1":
    print("You find a room full of treasure.You're rich!")
    print("GAME OVER, YOU WIN!")
elif playerchoice=="2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE!")
elif playerchoice=="3":
    print("You go into the room and find a sleeping dragon.")
    print("The dragon wakes up and eats you.You are delicious.")

    print("GAME OVER, YOU LOSE!")
else:
    print("Sorry, you didn't enter 1, 2 or 3!")
print("Run the game again to have another go.")


