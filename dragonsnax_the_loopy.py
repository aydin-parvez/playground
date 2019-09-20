#This is the final version.
#Do not delete!
import random

exitchoice = "Nothing"

while exitchoice != "EXIT":

    print("In front of you are four doors.You must choose one.")

    playerchoice = input("Choose 1,2,3 or 4...")
    if playerchoice == "1":
        print("You find a room full of treasure, you're rich!")
        print("GAME OVER, YOU WIN!")
    elif playerchoice == "2":
        print("The door opens and an angry ogre you with his club.")
        print("GAME OVER, YOU LOSE.")
    elif playerchoice == "3":
        print("You go into the room and find a sleeping dragon.")
        print("You can eithier:")
        print("1)Try to steal steal some of the dragon's gold.")
        print("2)Try to sneak around the dragon to the exit.")
        dragonchoice = input("Type 1 or 2...")
        if dragonchoice == "1":
            print("The wakes up and eats you.You are delicious.")
            print("GAME OVER, YOU LOSE.")
        elif dragonchoice == "2":
            print("You sneak around the dragon and escape the castle, blinking in the sunshine.")
            print("GAME OVER, YOU WIN!")
        else:
            print("Sorry, you didn't enter 1 or 2!")
    elif playerchoice == "4":
        print("You enter a room with a sphinix.")
        print("It asks you to guess what number  it is thinking of, between 1 and 10")
        number = int(input("What number do you choose?"))
        if number == random.randint(1, 10):
            print("The spinix hissed in disappointment.You guessed correctly.")
            print("She must let you free.")
            print("GAME OVER, YOU WIN!")
        else:
            print("The sphinix tells that your guess is incorrect.")
            print("You are now her prisoner forever.")
            print("GAME OVER, YOU LOSE.")
    else:
        print("Sorry you didn't enter 1, 2, 3 or 4!")

    exitchoice = input("Press return to play again, or type EXIT to leave.").upper()














    
    






























