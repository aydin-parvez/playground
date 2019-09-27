
aliens = 2
password = "SNAKE"

population = 7400000000

print()
print()
print("You need to activate the global defence network.")
print("Hope you know the password, for Earth's sake...")
print()
print("--------------------------------------------------------------------------------")
print("                    WELCOME TO THE GLOBAL DEFENCE NETWORK                       ")
print("--------------------------------------------------------------------------------")
print()

guess = input("Please enter the password:").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens**2
    print("There are", aliens, "aliens now on Earth.Try again!")
    if aliens > population:
        break
    print()
    print("Password hint:It's a reptile.")
    print()
    guess = input("Quick!Please enter the password:").upper()

if aliens > population:
    print("Noooooo!The aliens have  outnumbered us. All is lost.")
else:
    print("Hooray!We won the fight and the world is saved.")




