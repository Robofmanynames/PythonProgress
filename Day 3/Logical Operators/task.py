## If you want two arguments to be met, use the "and" operator
## the "and" logical operator has a few ways to check for accuracy:
## True and True = true
## False and True = False
## True and False = False


## If you want only one of your conditions to be met, you can use "Or"
## A and B = True
## A or B = True
## The only time you get a "False" reply with OR, is if both arguments
## are wrong and do no match what you are trying to determine


## The "not" operator is primarily based on changing the result of an
## argument to the opposite. False becomes True, True becomes False

## If you want to print multiple lines of text, like a picture or paragraph
## you can use 3 single quotes at the start and end '''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        ## a shorthand way to do this is: elif 45 <= age <= 55
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
