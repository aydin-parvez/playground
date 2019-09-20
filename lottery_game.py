print("Welcome to the lottery. Please type a number")
number = int(input("Enter a number."))
if number >=10:
   print("You win  $2000 from the lottery, you win!")
else:

    print("Aww, you lost!")
user_reply=input("Did you like the game(Type yes or no)")
if user_reply=="yes":
    print("Thank you.")
else:
    print("I'll make a better game")