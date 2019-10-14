import fun
number = fun.randint(1, 20)
guess = int(input("I'm thinking of a number from 1 to 20.What is it?"))
while guess != number:
    if guess < number:
        print("Your number was too low...")
    else:
        print("Your number was too high...")
    guess = int(input("Please try again..."))
print("Congratulations!Correct answer!")
user_reply=input("Did you like the game?")
if user_reply == "yes":
    print("Thank you.I'll put it in the internet")
else:
    print("I'll make a better game.")