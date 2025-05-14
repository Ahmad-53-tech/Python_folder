#1
#  score = []
#  for _ in score: What is the meaning of this statement.

#The underscore _ in the statement for _ in score: is a convention in Python that indicates the loop variable is not going to be used.
#Explanation:
#Normally, in a for loop, we assign each item from an iterable (like a list) to a variable.
#If we don’t actually need to use the variable inside the loop, we use _ as a placeholder.




#2.
correct_username = "Ahmad53"
correct_password = "PY2025"

for attempts in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Wrong User Input")
else:
    print("Too many attempts. Access denied.")




# Exercise 3: Print Odd Numbers Between 1 and 50.
#Use a while loop to print all odd numbers between 1 and 50.
number = 1
while number <= 50:
    if number % 2 != 0:
        print(number)
    number += 1


# Exercise 4: Find the largest digit in a number.
#Take an integer as input and find the largest digit in it using a while loop.
largest_digit = -1
number = int(input("Number: "))
while number > 0:
    digit = number % 10
    if digit > largest_digit:
        largest_digit = digit
    number = number // 10
print(f"The largest digit is {largest_digit}")


# Exercise 5: Reverse a Number.
#Write a program that takes an integer as input and prints its reverse.
number = int(input("Enter an integer(to get the sum of the digits): "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print(f"The reversed number is {reverse}")


# Exercise 6: Find the sum of digits in a Number.
#Take a number as input and calculate the sum of its digits.
number = int(input("Enter an integer(to get the sum of the digits): "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
print(f"The sum of the digits is: {sum_of_digits}")


# Exercise 7: Check if a number is a Palindrome.
#Write a program to check if a given number is a Palindrome.
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0

number = abs(number)
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")



# Exercise 8: Count Vowels in a string
#Take a string as input and count the number of vowels (a,e,i,o,u) in it using a while loop.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
index = 0
while index < len(string):
    if string[index] in vowels:
        vowel_count += 1
    index += 1
print(f"Number of vowels in the string: {vowel_count}")
