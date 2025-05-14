#1.
#Library Book Borrowing
#  You have a list of books you want to borrow from the library.
#  Rules:
#  If a book is unavailable, skip it.
#  Once all available books are borrowed, print "Borrowing done!"


books_to_borrow = ["Harry Potter", "The Hobbit", "Love", "To Kill a Mockingbird"]
available_books = ["Harry Potter", "Love"]  

for book in books_to_borrow:
    if book not in available_books:
        continue  
    print(f"Borrowed: {book}")

print("Borrowing done!")

#2
#Packing for a Trip
#  You have a list of items to pack for a trip.
#  Rules:
#  If an item is missing or unavailable, skip it.
#  Once all available items are packed, print "Packing done!"

packing_list = ["Shirt", "Pants", "Shoes", "Sunglasses", "Toothbrush"]
available_items = ["Shirt", "Shoes", "Toothbrush"]  

for item in packing_list:
    if item not in available_items:
        continue  
    print(f"Packed: {item}")

print("Packing done!")


#3.
#Recipe Ingredients Check
#  You have a list of ingredients needed for a recipe.
#  Rules:
#  If an ingredient is missing, skip it.
#  Once all available ingredients are gathered, print "Ready to cook!"

recipe_ingredients = ["Eggs", "Milk", "Flour", "Sugar", "Butter"]
available_ingredients = ["Eggs", "Milk", "Butter"]  

for ingredient in recipe_ingredients:
    if ingredient not in available_ingredients:
        continue  
    print(f"Added: {ingredient}")

print("Ready to cook!")



#4.
# Generating a school Timetable.
# A school has 5 days (Monday-Friday) and 6 periods per day.
# Write a nested loop that prints a timetable with "Day X - Period Y".

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = 6

for day in days:
    for period in range(1, periods + 1):
        print(f"{day}: Period {period}")



#5.
#A cinema has 5 rows and 10 seats per row.
#Write a nested loop that prints seat numbers like: 
#"Row 1 - Seat 1", "Row 1 - Seat 2", … "Row 5 - Seat 10".

rows = 5
seats_per_row = 10

for row in range(1, rows + 1):
    for seat in range(1, seats_per_row + 1):
        print(f"Row {row} - Seat {seat}")



#6.
#Parking Lot Simulation:
#A parking lot has 3 levels, with 4 rows of cars per level, and 5 spots per row.
#Write a nested loop that prints the position of each car in the format: "Level X - Row Y - Spot Z".

levels = 3
rows = 4
spots_per_row = 5
for level in range(1, levels + 1):
    for row in range(1, rows + 1):
        for spot in range(1, spots_per_row + 1):
            print(f"Level {level} - Row {row} - Spot {spot}")



#7.
# Chessboard Pattern:
#A chessboard has 8 rows and 8 columns (black and white squares).
#Write a nested loop to print a pattern representing a chessboard using # for black and . for white.

board_size = 8

for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 0:
            print(".", end=" ")  # White square
        else:
            print("#", end=" ")




#8.
# Hotel Room Booking:
#A hotel has 3 floors, with 10 rooms per floor. Some rooms are booked.
#Write a loop to check the availability of rooms and display 
# "Room X on Floor Y is Available" if it's free.

floors = 3
rooms_per_floor = 10
booked_rooms = {(1, 3), (2, 5), (3, 8)}  

for floor in range(1, floors + 1):
    for room in range(1, rooms_per_floor + 1):
        if (floor, room) not in booked_rooms:
            print(f"Room {room} on Floor {floor} is Available")

print()
for k in range(4):
    for f in range(4):
        print("# ",end="")
    print()

print()
for k in range(4):
    for f in range(k+1):
        print("# ",end="")
    print()

print()
for k in range(4):
    for f in range(4-k):
        print("# ",end="")
    print()


print()
rows = 4

for i in range(1, rows + 1):
    for j in range(i, rows + 1):
        print(j, end=' ')
    print()

print()
num = int(input("Enter a number to check if it is prime or not: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not Prime")
        break
else:
    print(f"{num} is Prime")


