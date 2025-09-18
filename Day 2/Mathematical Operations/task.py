# Implicit Type casting

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) # python makes this a floating point number
print(6 // 3) # python makes this a whole number integer

#Implicitly converting the result into a floating point number. We don't always want that.
# Using // it will essentially do what normal division does in the system, but it goes through and removes
# all of the decimals to make it a whole number
## Sometimes this makes a big problem, because if you divide a number that has decimals, // will remove them
# for example:

print( 5 / 3) # will print the number with decimals
print( 5 // 3 ) # will print the whole number and removes the decimals

## If you want to create an answer by using exponents (two to the power of two, for example) use two **'s

print(2**2)

## Python uses PEMDAS in its way to plugging code when you write it and print it out
### Also good to know if you want to comment out a bunch of stuff at once, highlight/select and type CTRL and /

# ()
# **
# * OR /
# + OR -

## Also good to know that when following PEMDAS, python will use the order from left to right when prioritizing
## multiplication and division

print(3 * 3 + 3 / 3 - 3)
#Solve - what will it do first?
## My answer: 3 * 3 is first = 9, 3 / 3 = 1 is second, and then 9 + 1 - 3 = 7. The answer would be 7.

#PAUSE 2 problem: Change the code so it outputs 3
print( 3 * 3 + 3 / 3 - 3)
# I couldn't figure it out fast enough. The answer is:
print( 3 * (3 + 3) / 3 - 3)
# Adding the parenthesis in this problem, helped to create just the right amount to be subtracted at the end