name = input("Enter your name: ")
age = int(input("Enter your age: "))
height =  float(input("How tall are you(cm)? "))

if age >= 18:
    if height >= 170:
        print(f"Good day {name}, you have been accepted into our GYM.")
    else:
        print(f"Good day {name}, you are not accepted because you aren't up to 170cm.")
else:
    print("Sorry, you are not accepted because you are less than 18.")
