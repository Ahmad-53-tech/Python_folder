#Dictionaries is a collection of key value pairs.



customer = {
    "Name": "Fatima ",
    "Age": 70,
    "is_verified": True

}
print(customer["Name"])#if we use this one and run the code if the key doesn't exist, it will show "Key Error".

#or

print(customer.get("Name"))#But if we use this one and run the code if the key doesn't exist, it will show "None".

customer["birthdate"] = "1st January, 1954" # Adding a key is also allowed.



# updating a key is allowed in the dictionary.



dictionary = {"Age": "19",
              "Course": "Python",
              "Color": "Green"}
for a in dictionary:
    print(dictionary[a])



dictionary = {"Age": "19",
              "Course": "Python",
              "Color": "Green"}
for a in dictionary:
    print(a)







