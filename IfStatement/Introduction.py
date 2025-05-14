#Write a program to accept time in 24Hrs format and then greet the user.
    #Time between 0-12 : Good Morning
    #Time between 13-16 : Good Afternoon
    #Time between 17-20 : Good Evening
    #Time between 21-24 : Good Night
    #Otherwise: Wrong Input

time = int(input("Enter a your current time in 24hrs format: "))

if 12 >= time >= 0:
    print("Good Morning! ")

if 16 >= time > 12:
    print("Good Afternoon! ")

if 20 >= time > 16:
    print("Good Evening! ")

if 24 >= time > 20:
    print("Good Night! ")

else:
    print("Wrong Input")




