print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
stage_one = input('''You are at a crossroad. Where do you want to go? \n
Type "Left" or "Right"\n''')
if stage_one == "left" or "Left":
    print("You arrive at a flooded land bridge leading to the other side where you see a corridor within dark caves.")
else:
    print("Fall into a hole. \nGame Over.")

stage_two = input('''Do you take your chances and ford the land bridge? 
    Or will you wait out the flooding to cross? 
    Type "Swim" or "Wait \n"''')
if stage_two == "Wait" or "wait":
    print("You are now inside the corridor of the caves and see three doors.\n"
          "A red, yellow, and blue door.")
else:
    print("Attacked by trout.\n"
          "Game Over.")

stage_three = input('''You hear ominous noises behind two doors. \n
Which door will you choose?\n
Type "Red" "Yellow" or "Blue" to continue.\n''')
if stage_three == "Red" or "red":
    print("Burned by fire."
          "Game Over.")
elif stage_three == "Blue" or "blue":
    print("Eaten by beasts."
          "Game Over.")
elif stage_three == "Yellow" or "yellow":
    print("You Win!")
else:
    print("Game Over.")

print("You won the game! You found the treasure and were able to escape!")



##This is Angela's code:
## Angela used a backslash to escape single quote issues and text speech.
## I used the three single quotes, so mine might not be the best approach?
## best practice is to change the user's input to upper or lower function
## this will change the text written to your preferred method for easier
## coding, and you don't have to type like how I did in my code above.
## example: input("blah blah).lower()


choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        "There is a house with 3 doors."
                        "One red, one yellow, and one blue."
                        "Which color do your choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")