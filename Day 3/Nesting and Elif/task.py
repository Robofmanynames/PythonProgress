print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    # age = int(input("What is your age?"))
    # if age <= 18:
    #     print("Please pay $7.")
    # else:
    #     print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

# The commented sections above were added if we wanted to create a complex problem
# where we must learn the age of the person to determine how much they would owe


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

# In this example, we are now using a third argument using Elif

## It is important to know and remember that you can use as many elif conditions
## as you want between an if and else block