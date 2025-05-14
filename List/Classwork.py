# . List
#a. Create a list of five numbers and:
# * Find the sum of all numbers.
# * Find the largest number in the list.
# * Sort the list in ascending order.
#b. Given the list fruits = ["apple","banana", "cherry", "date", "fig1"], perform the following:
# * Add "grape" to the list.
# * Remove "banana" from the list.
# * Reverse the list.
numbers = [2, 11, 5, 20, 15]
total = 0
largest_number = numbers[0]
for number in numbers:
    total += number
print(f"Sum: {total}")
for number in numbers:
    largest_number += 1
    if number > largest_number:
        largest_number =  number
print(f"Max: {largest_number}")
numbers.sort()
print(numbers)
fruits = ["apple", "banana", "cherry", "date", "fig1", "grape"]
fruits.remove("banana")
fruits.reverse()
print(fruits)