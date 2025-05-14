#1.
# Variables and Input

#•	Write a program that:
#a.	Asks the user for their name and age.
#b.	Stores these values in variables.
#c.	Prints a greeting message using the stored variables.

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name +"!," + " you are " + age + " years old.")


#2.
# Arithmetic Operators

#•	Write a program that:
#a.	Asks the user for two numbers.
#b.	Performs addition, subtraction, multiplication, division, and modulus operations.
#c.	Prints the results.

num_1 = float(input("Enter any number of your choice: "))
num_2 = float(input("Enter another number of your choice: "))

# For Addition
sum = num_1 + num_2
print("For Addition your answer is:" , sum)

# For Subtraction
subtraction =num_1 - num_2
print("For Subtraction your answer is:" , subtraction)

# For Multiplication
multiplication = num_1 * num_2
print("For Multiplication your answer is:" , multiplication)

# For Division
division = num_2 / num_1
print("For Division your answer is:" , division)

# For Modulus
modulus = num_1 % num_2
print("For Modulus your answer is:" , modulus)


#3.
# Operator Precedence

#• Predict the output of the following expressions, then verify by running them:

#print(10 + 5 * 2)
#print((10 + 5) * 2)
#print(20 / 5 + 3)
#print(20 / (5 + 3))

# Predicting the answers
equation_1 = 20
equation_2 = 30
equation_3 = 7
equation_4 = 2.5

# Running them
print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))


#4.
#•	Write a program that:
#a.	Ask the user to input their weight (as a float) and height (as an integer).
#b.	Displays the type of each input using the type() function.

weight = float(input("Enter your weight: ")) 
height = float(input("Enter your height: "))

print(type(weight))
print(type(height))


#5.
#•	Write a program that:
#a.	Asks the user to input a number as a string.
#b.	Converts it to an integer and a float.
#c.	Prints the results of these conversions.

number = input("Input a number: ")
int_conversion = int(number)
float_conversion = float(number)

print("Integer:", int_conversion)
print("Float:", float_conversion)


#6.

#•	Write a program that:
#a.	Asks the user to input two numbers.
#b.	Asks the user to choose an operator (+, -, *, /).
#c.	Performs the chosen operation and displays the result.

num_1 = float(input("Input a number: "))
num_2 = float(input("Input another number: "))

chosen = input("Choose an operator(+, -, *, /): ")


if chosen == "+":
    print("You chose the addition operator")
    print("For your addition your answer is" , num_1 + num_2)

elif chosen == "-":
    print("You chose the subtraction operator")
    print("For your subtraction your answer is" , num_1 - num_2)

elif chosen == "*":
    print("You chose the multiplication operator")
    print("For your multiplication your answer is" , num_1 * num_2)

elif chosen == "/":
    print("You chose the division operator")
    print("For your division your answer is" , num_1 / num_2)

else:
    print("Invalid Operator")


#7.
#•	Write a program to swap the values of two variables without using a third variable.

a = input("Enter something: ")
b = input("Enter something: ")

print(f"({a}, {b})")

# a = b #2 to 5
# b = a # 5

a, b = b, a

print(f"({a}, {b})")


#8.
#	Write a program that:
#a.	Ask the user to input an integer.
#b.	Check whether the number is even or odd.

input = int(input("Enter any number: "))

if input%2 == 0:
    print("You chose an even number")
else:
    print("You chose an odd number")
    


#9.
#•	Write a program that:
#a.	Ask the user to input an integer.
#b.	Check whether the number is even or odd.

p = float(input("Enter a principal amount: "))
r = float(input("Enter a rate: "))
t = float(input("Enter a time(in years): "))

SI = (p * r * t) / 100.
print("Your Simple Interest is", SI)


