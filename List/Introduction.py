sales = []
for i in range(1, 7):
    s = input("Enter your sale for the day: ")
    sales.append(s)
sales.sort()
sales.reverse()
print(sales)




numbers = [10, 6000, 332, 31333331, 31, 5432, 22234, 3342, 123, 4567890, 65432123456, 34567843216532]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
         largest_number = number
print(largest_number)




numbers = [1,2,4,5,1,2,4,5,4,2,2,2,1,3,1,2,2,5,3,2,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)



fruit = ["apple", "banana", "cherry", "1", "2"]
print(fruit[0:3])
print(fruit[3:])