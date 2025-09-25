import random
## This is how we import the "Random" module
## A module is the file I am working on with all of this code.
## When you have long projects, or multiple projects, you can break them
## up into portions and create modules to put it all into one code sheet

## How to create your own module:
## Right click on the left (Course) where it says "Random Module" and
## right click it. Options will include "New" near the top. Click it.
## From there, select "New Python file" near the middle.
## Name the file. And now you can work on it.
## Back in your main code file "Task.py" or "Main.py", you have to import it.
## Do "import "name of your python file"
## Once that is written, now you can call what you have in that file.


random_integer = random.randint(1,10)
print(random_integer)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)
random_number_0_to_1 = random.random() *10
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)


## PAUSE 1 Task - Create a coin flip

print("Heads")
print("Tails")

