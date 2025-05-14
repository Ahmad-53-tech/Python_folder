#1.
numbers = [5, 3, 5, 3, 5, 3]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)



#2.
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


#3.
shirts = ["red", "blue"]
shorts = ["black", "white", "grey"]

for shirt in shirts:
    for short in shorts:
        print("Wearing", shirt, "shirt with", short ,"short")




#4.
correct_username = 'Ahmad53'
correct_password = 'PY2025'


max_attempts = 3
for attempt in range(1, max_attempts + 1):
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == correct_username and password == correct_password:
        print('Successful login')
        break
    else:
        print(f'Wrong user input. Attempt {attempt} of {max_attempts}.')
        if attempt == max_attempts:
            print('Maximum login attempts reached. Access denied.')


for x in range(1, 5):
    for y in range(1, 5):
        print(f"{x} X {y} = {x * y}")
        print("_"*10)