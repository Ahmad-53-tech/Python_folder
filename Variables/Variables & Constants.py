# SECTION 1: VARIABLES AND CONSTANTS
#1.
# Variables are containers that hold values that can change during program execution
# x = 10 # Here, 'x' is a variable that holds the value 10.
# x = x + 5 # The value of 'x' is now updated to 15
# Contents are fixed values that do not change during program execution
# PI = 3.14159 
#'PI' is treated as a constant.

#2.
# Assigning Value
name = "Princess"
print(name)

# Modifying it (1)
name = "Elijah"
print(name)

# Modifying it (2)
name = "Esther"
print(name)

# Assigning Constant
print("Hello World")

# Modifying the Constant
print("Hello Guys")

# The program allowed the value to be changed, but normally it is not supposed to.
# Constants are fixed values, so it should be understood that it is not
# supposed to be changed

#3.
age = int(input("Enter your age: "))
years_until_100 = 100 - age
# Displaying the result
if years_until_100 > 0: print("You are above 100 years")

if years_until_100 == 0:
    print("Congratulations! You are 100 years old.")

if years_until_100 < 100:
    print("You will turn 100 in" , years_until_100 , "years")


#SECTION 2: DATA TYPES
#1.
#Integer: They represent whole numbers, positive or negative without decimals.
#E.g., 1, 20, 53 etc.

#String: They represent sequences of characters enclosed in single
# or double quotes. E,g. name = "Ahmad", Greetings = 'Good morning' etc.

#Boolean: They represent true or false value. E.g. i_am_robot = False
#i_am_human = True

#Float: They represent numbers with decimals. E.g. 3.14, 9.0, 8.55 etc.

#Nonetype = They represent null value. E.g., Result = None etc.

#Set = They represent unordered collection of unique items.
# E.g. (1, 2, 3, 4, 5) etc.

#Dictionary = They are a collection of key-value pairs, where keys are unique.
# E.g., Person = ("name": "Serwaa", "age": 30, "City": "Accra")

#List = An ordered collection of items, which can be of mixed data types.
#fruits = ["apple", "banana", "cherry"]
#mixed_list = [1, "hello", 3.5, True]

#Tuple = An ordered unchangeable collection of items.
#coordinates = (10.0, 20.0)
#user_info = ("Alice", 30, "Engineer")


#2.
string_input = input("Enter a string: ")
print(type("string_input"))

int_input = input("Enter an integer: ")
print(type("int_input"))

float_input = input("Enter a float: ")
print(type("float_input"))

bool_input = input("Enter a boolean: ")
print(type("bool_input"))

#3.
name = input("Enter your name: ")
print(type(name))

age = int(input("Enter your age: "))
print(type(age))

height = float(input("Enter your height in meters: "))
print(type(height))

print("Hello",name +"!"+"," ,"You are",age,"years old and your height is",height,"meters")


#SECTION 3: OPERATORS
#1.
#Arithmetic Operators = Used to perform mathematical operations.
#they are (+,-,/,*,**,%)
#E.g. x=3, y=5, z=6. Calculate c=(y**x+5-z)%2
#c=0

#Comparison Operators = Used to compare two values and return a Boolean result.
#they are (==, !=, <=, >=, <, >.)
#E.g.
#x = (10 == 5)  # x = False
#y = (10 != 5)  # y = True
#z = (10 > 5)  # z = True
#a = (10 < 5)  # a = False
#b = (10 >= 5)  # b = True
#c = (10 <= 5)  # c = False

#Logical Operators = Used to combine conditional statements.
#they are (AND, OR NOT).
#E.g., x = (True and False) # x = False
# = (True or False) # y = True
#z= not True # z = False

#Assignment Operators = Used to assign values to variables.
# we have only one, and it is the "="

#2.
length = int(input("Enter the length of a rectangle: "))
width = int(input("Enter the width of a rectangle: "))

area = length * width
print("Area is",area,"cm²")

perimeter = 2 * (length + width)
print("Perimeter is",perimeter,"cm")

#3.
num1 = float(input("Enter any number of your choice: "))
num2 = float(input("Enter another number of your choice: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 
modulus = num1 % num2 
exponential = num1 ** num2

print("For addition your answer is",addition)
print("For subtraction your answer is",subtraction)
print("For multiplication your answer is",multiplication)
print("For division your answer is",division)
print("For modulus your answer is",modulus)
print("For exponential your answer is",exponential)

#3.
Question1 =int(input("What is the result 20*10? "))
result_for_the_question = 400 - Question1
# Displaying the result
if result_for_the_question == 200: print("correct")
if result_for_the_question > 200: print("Wrong")
if result_for_the_question < 200: print("Wrong")

Question2 = int(input("What is the result of 40 * 5? "))
result_for_the_question = 400 - Question2
# Displaying the result
if result_for_the_question == 200: print("correct")
if result_for_the_question > 200: print("Wrong")
if result_for_the_question < 200: print("Wrong")

Question3 = int(input("150+50? "))
result_for_the_question = 400 - Question3
# Displaying the result
if result_for_the_question == 200: print("correct")
if result_for_the_question > 200: print("Wrong")
if result_for_the_question < 200: print("Wrong")

if Question1 and Question2 != 200 : print("Your final score is 1 out of 3.")
if Question1 and Question3 != 200: print("Your final score is 1 out of 3.")
if Question2 and Question3 != 200: print("Your final score is 1 out of 3.")
if Question1 and Question2 and Question3 == 200: print("Your final score is 3 out of 3.")















