# A function is a container for few lines of code that performs a specific task.
#We have two types of functions. They are Parameterized and unparametarized function. 
# - Parametized function: They take values inside the function's parenthesis
# - Unparametized function: They do not take values inside the function's parenthesis


def greet_user():
    print("Hi user!")
    print("Welcome aboard") 


print("Start")
greet_user()
print("Finish")

#1.
# Parameters: They are variables used in your functions.
# Argument: They are values your parameters work with.


def greet_user(name):
    return f"Hello {name}"

user_name = input("Enter your name: ")


print(greet_user(user_name))



#2.
def add_number(num1, num2):
    return num1 + num2

first_input = int(input("Enter a number: "))
second_input = int(input("Enter another number: "))

result = add_number(first_input, second_input)
print(result)


#3.
def get_user_info(name, age, course):
    return f'Hello {name}, you are {age} years old. You are offering {course}'

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_course = input("Enter your course: ")


result = get_user_info(user_name, user_age, user_course)
print(result)




#Exercises:
#1.
# Write a function that takes a number and returns even if it is even and old if it is old.


def even_or_odd(number):
    if num % 2 ==0:
        return 'Even'
    return 'Odd'


num= int(input("Enter a number: "))

print(even_or_odd(num))


#2.
# Write a function that takes two numbers and returns the larger one.


def find_larger(num1, num2):
    if num1 > num2:
        return num1
    return num2

number1 =  int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(find_larger(number1, number2))


#3.
# Write a function that converts a temperature from celcius to Fahrenheit.
# Using the Formula F=(C*9/5)+32

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32


num= int(input("Enter your temperature in celcius: "))



print(celcius_to_fahrenheit(num))


#4.
# Write a function that takes a number, returns positive, negative or Zero.

def users_number(num1):
    if num1 > 0:
        return "Positive"
    elif num1 < 0:
        return "Negative"
    return 0

number1 = int(input("Enter a number: "))

print(users_number(number1))




bal = 50
def balance():
    return bal

def deposit(amt):
    global bal
    bal = bal + amt
    return bal

def withdraw(amt):
    global bal
    if amt > bal:
        return "Insufficient Funds"
    else:
        bal -= amt
        return bal

deposit(100)
print(withdraw(20))


deposited_amount = int(input("Deposited Amount: "))
withdrawal_amount = int(input("Withdrawal Amount: "))


deposit(deposited_amount)
print(f"Balance: {withdraw(withdrawal_amount)}")