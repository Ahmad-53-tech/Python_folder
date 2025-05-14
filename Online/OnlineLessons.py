course = "Lets Gist"
print(course.upper())
First = float(input("Enter a number: "))
Second = float(input("Enter another number: "))
largest_number = First + Second
print(f"Your added value is ={largest_number}")
a = 1
while a <= 5:
    print(a)
    a = a + 1
i = 1
while i <= 10:
    print (i * "$")
    i = i + 1
names = ["Ahmad", "Elijah", "Esther", "Princess"]
numbers = {1,2,3,4,5}
numbers.add(6)
print(numbers)


first = "John"
last = "Smith"
#f: formatted 
msg = f'{first} [{last}] is a code.'
print(msg)

course = 'Python for beginners'

# replace: to replace values
print(course.replace('beginners', "Absolute beginners"))

#find: to find a value but returns in index
print(course.find('g'))

#len: to count the number of characters in a string
print(len(course))

#upper: to turn the string to Upper Case
print(course.upper())

#in: to check whether a word is present gives an answer in boolean
print('Python' in course)

# functions specifically for strings are call method

#round: to round up a number
x = 52.9
print(round(x))

#abs: absolute value
x = 52.9
print(abs(-x))

#import math: to import reusable maths functions

#Exercise 1
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

#Logical operators
# AND: both conditions must be true
# OR: at least one condition must be true

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print()

