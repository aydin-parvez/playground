import datetime

year_birth = int(input("Enter your date of birth."))
year_now = datetime.date.today().year
age = year_now - year_birth
print("You are", age, "years old")