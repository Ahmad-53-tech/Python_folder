count = 0

while count <= 10:
    print(count)
    count += 1


count = 1

while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1


number = 5

while True:
    user_guess = int(input("Guess: "))

    if user_guess == number:
        print("You nailed it🎯")
        break
    elif user_guess == number:
        continue
    else:
        print("Try Again.....")




count = 10

while count <= 10:
        if count >= 1:
            print(count)
        count -= 1
        break


number = int(input("Enter a number to get its factorial: "))
factorial = 1
count = 1

while count <= number:
      factorial *= count
      count += 1
print(f"Factorial: {factorial}")





number = int(input("Number: "))
count = 1

while count <= 10:
      print(f"{number} x {count} = {number * count}")
      count += 1






for i in range(3):
    code = input("Enter a code: ").strip()
    if code == "*312#":
        print("""
        1. Buy Data
        2. Housing
        3. Transfer""")

        data = input("Enter a plan: ").strip()
        if data == "1":
                print("""
                        1. 100 for 100MB
                        2. 200 for 250MB
                        3. 400 for 400MB""")
                chosen = input("Choose: ").strip()
                if chosen == "1":
                    print("You have successfully purchased 100MB. Your data bundle will expire by 3/11/2025.")
                elif chosen == "2":
                    print("You have successfully purchased 200MB. Your data bundle will expire by 5/11/2025.")
                elif chosen == "3":
                    print("You have successfully purchased 400MB. Your data bundle will expire by 10/11/2025.")
                else:
                    print("Wrong Input")
                break

        elif data == "2":
            print("Call this number +2349123852253")
            break
        elif data == "3":
            print("Use your Bank App, IDIOT!")
            break
        else:
            print("Wrong Input")
            break

