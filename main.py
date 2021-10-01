print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Tickets are $5.")
    elif age <= 18:
        print("Tickets are $7.")
    else:
        print("Adult tickets are $12.")
    
else:
    print("Sorry, you must grow taller before you can ride.")