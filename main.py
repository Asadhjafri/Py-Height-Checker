print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Can Ride rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
      print("Please pay 5 dollars")
    elif age <= 18:
        print("Please pay 7 dollars.")
    else:
        print("Please pay 12 dollars.")
else:
    print("Can't ride rollercoaster")
