# - Dictionaries
#a. Create a dictionary to store the names of three students and their respective scores. Perform the following:
# * Retrieve the score of one student.
# * Add a new student and their score.
# * Update the score of an existing student.
#B. Given the dictionary: student_info = {"Alice": 25, "Bob" : 22, "Charlie": 24}
# * Print all the keys in the dictionary.
# * Print all the values in the dictionary.
# * Check if "David" exists in the dictionary.
my_dictionary = {"Ahmad": 92,
                 "John": 76,
                 "Ada": 78}
print(f"Ahmad's Score: {my_dictionary.get('Ahmad')}")
my_dictionary["Joseph"] = 80
my_dictionary["Ahmad"] = 100
print(my_dictionary)
student_info = {"Alice" : 25,
                "Bob" : 22,
                "Charlie" : 24}
for key in student_info:
    print(key)
for key in student_info:
    print(student_info[key])



#Exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"


}
output = ""
for digit in phone:
    output += digits_mapping.get(digit, "Unavailable") + " "
print(output)