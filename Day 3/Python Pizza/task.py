print("Welcome to Python Pizza Deliveries!")

## The reason my code didn't work, was because my IDE did not
## recognize the variable "cost" from the beginning. It figured that
## if I am trying to give it an option to be defined, it might not
## get defined and create errors. Rule of thumb, define the variable
## at the very beginning to avoid this error. EX: cost = 0

cost = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    cost = 15
elif size == "M":
    cost = 20
elif size == "L":
    cost = 25
else:
    print("You typed the wrong inputs.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is: ${cost}.")

## This is what I came up with. Below is Angela's solution

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs.")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")