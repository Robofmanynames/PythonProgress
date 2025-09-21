from logging import StringTemplateStyle

bmi = 84 / 1.65 ** 2

print(bmi)
# this will print out 30.853994...
# if we wrap in int(), it will round the number down to the lowest whole number

print(int(bmi))
# this is called Flooring the number
# we can use something more accurate with the Round function

print(round(bmi))
# obviously like in math, it will round up or down based on the full decimal length
# you can also determine how much rounding you can do with the number of digits
# you would like to include in the rounding process. Like 2, 3, or 4 decimal places

print(round(bmi,2))
# round(*variable* , *enter the number of decimal places for rounding))

# Assignment Operators - Really Important here!
# In an example of keeping score in a game, you would do the following:
# score = 0
# We determine that the score will begin at zero for the beginning of the game
# Anytime the player gets a point, you might want to make a code that looks like this:
# score = score + 1
# And you would also do this for losing points, by using subtraction, etc. etc.
# There is a shorthand version of this where instead of typing it all out twice, you can do:
# score += 1 which is the shorthand for score = score + 1
# Much easier to read and do. You can do this with +=,-=,*=, and /=
score = 0
score += 1
print(score)

# F-Strings
# In Python, you can use F-Strings to allow shortcuts in using multiple data types
# inside one specific set of parenthesis when coding. For example, if you want to use:
# print("Your score is " + str(score))
# Instead of changing multiple variables into integer or string, you can just substitute
# with  f   before the quotes and if you want to insert a variable, use curly brackets {}.
# Now you don't have to use int() or str() or even use + to put code together, unless you're
# using addition or subtraction within the code for mathematical processes.
# Example:
# score = 0
# height = 1.8
# is_winning = True
#
# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
# All the data types get combined into a full string using the quick f-string process to
# make it easier to type it all easily.
