print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Can Ride rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
      bill = 5
      print("Child tickets are 5 dollars")
    elif age <= 18:
      bill = 7
      print("Youth tickets are 7 dollars.")
    else:
      bill = 12
      print("Adult tickets are 12 dollars.")
    wants_photo = input("Do you want a photo taken? Yes or No") 
    if wants_photo == "Yes":
else:
    print("Can't ride rollercoaster")
