#Loops allows us to execute a block of code multiple times without writing repetitive code manually.
# The types of loops are While loops and for loops.
# While loops: They execute some code while some conditions are true.
# For loops: They execute a block of code for a fixed number of times. it can be used to iterate over a range, sequence, and string.
#it can also be used to construct a definite loop.
# break: it allows us to exit a loop


name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}") 


age = int(input("Enter a number: "))
while age < 1 :
    print("Enter a positive number")
    age = int(input("Enter a number: "))
print(f"Your are {age} years old.")

balance = 1000000000000000000000
while True:
    print(f"Current balance: ${balance}")
    amount = int(input("Enter withdrawal amount (multiple of 10, or 0 to exit): "))
    if amount == 0:
        print("Transaction complete.")
        break
    if amount % 10 != 0:
        print("Invalid amount! Please enter multiple of 10")
    elif amount > balance:
        print("Insufficient funds! try a smaller amount.")
    else:
        balance -= amount
        print(f"Withdrawal Successful! you withdrew ${amount}.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in numbers:
    print(item)
numbers = range(5)
for number in numbers:
    print(number)

for number in range(5, 20, 2):
    print(number)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

