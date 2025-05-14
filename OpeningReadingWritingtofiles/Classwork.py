# 1. Create a text file named student.txt and write the following names into it, each on a new line: Alice, Bob and Charles.
# 2. Write a program to read the content of student.txt and print each name on your terminal using a loop.
# 3. Add two more names David and Emma to student.txt without deleting the previous content.

with open("Student.txt", mode='w') as file:
    file.write('Alice\n')
    file.write('Bob\n')
    file.write('Charles\n')

with open("Student.txt", mode='r') as file:
    contents = file.readlines()
    for a in contents:
        print(a)

with open("Student.txt", mode='a') as file:
    file.write('David\n')
    file.write('Emma')



