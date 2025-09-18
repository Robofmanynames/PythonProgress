print(len("12345"))

print(type("Hello"))
print(type(12345))
print(type(False))
print(type(123.45))

# Data Conversion / Type Casting - changing from one to another like string to integer
# int is a way to make the string turn into an integer
int("123") #will convert this string to an integer

print("123" + "456")
# this would concatenate both strings into: 123456 and it is still string data type
# by adding 'int()' to the string, it turns into an integer, and now "+" is treating like addition
print(int("123") + int("456"))
#this will add 123 with 456 and prints out the answer

# Sometimes you can't convert things into a different data type:
# examples: 'abc' can't be converted into an integer number
# You can lose data like this at-large if you do not carefully inspect your information you are converting

#Pause Problem - Make this line of code run without errors
yourname = input("Enter your name: \n")
print("Number of letters in your name: ",len(yourname))

## While this may have worked, Angela provides the following solution. Because your variable name comes up
## as an integer (maybe?), the "+" within the print line in the original code line might come up with errors.
## You will want to check the data types, and then wrap the integer (the variable name) in string parenthesis

#Angela's code:
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int
#Solution
print("Number of letters in your name: " + str(length_of_name))


