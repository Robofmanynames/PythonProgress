print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

# In this lesson, we learned that if/elif/else is used for determining the result
# of only one of these conditions coming true, with the code reading down procedurally
# If you want multiple conditions to occur, you can do multiple ifs so that they will
# all be executed
# To review: if/elif/else is for one condition to be met. Multiple ifs - all conditions


## New Example using multiple ifs ##

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
# In this same if statement block, go down two lines, to create your new prompt
    wants_photo = input("Do you want to have a photo taken? Type Y for yes and N for No")
    if wants_photo == "Y":
#Add $3 to the bill, and create "bill" variable to the age verification
        bill = bill + 3 #or you can write it as bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")