student_list = []
username = input("Enter your Username: ").strip()
password = input("Enter your Password: ").strip()

while True:
    if username == "Ahmad53" and password == "PY2025":
        print(f"""
                    1. Add student
                    2. Delete Student
                    3. Exit""")
        chosen = input("Choose your preferred option: ")
        if chosen == "1":

            amount_of_students = int(input("How many students do you want to add: "))
            for i in range(amount_of_students):
                add_student = input("Add a student: ")
                student_list.append(add_student)
            student_list.sort()
            student_list.reverse()
            print(student_list)
            move = input("Do you want to continue: ").lower()
            if move == "yes":
                continue
            if move == "no":
                break
        elif chosen == "2":
            if not student_list:
                print("Kindly add a student record")
                continue
            else:
                name_removal = input("Enter the name you want to remove: ")
                student_list.remove(name_removal)
                print(student_list)
                move = input("Do you want to continue: ").lower()
                if move == "yes":
                    continue
                if move == "no":
                    break
        elif chosen == "3":
            break


