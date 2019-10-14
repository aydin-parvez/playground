while True:
    try:
        number = int(input("Enter a number to see the square number."))
    except ValueError:
        print('Hey!! that is not a number. Try again...')
        continue
    print(number*number)
    again = input("Press Y to try again or N to stop.").upper()
    if again == "Y":
        continue
    else:
        break