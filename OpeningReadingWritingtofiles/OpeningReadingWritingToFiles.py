# OPENING, READING AND WRITING TO FILES.
# We have to manually close using this method.
file = open("my_file.txt")
contents = file.read()
#print(contents)
file.close() # Important because after opening the file, it takes up resources in your computer just like opening many tabs in a browser.


# Sometimes it's hard to remember to close the file because you might be doing so many things in between the open and close. Closes automatically.
with open('my_file.txt') as file:
    content = file.read()
    print(content)


# Write to the file - overwrites completely. If a file does not exist, creates it from scratch (only in written mode.)
with open('my_file.txt', mode= "w") as file:
    print(file.write('Yes we can be friends!'))


# Appends to the file, does not overwrite, only adds.
with open('my_file.txt', mode='a') as file:
    print(file.write('\nWe have so much in common!'))