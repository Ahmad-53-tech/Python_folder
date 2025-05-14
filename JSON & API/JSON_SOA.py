#JSON - JavaScript Object Notation
#API - Application Programming Interface


#                               WHAT IS JSON
# - JSON: It is a lightweight data format used for exchanging data between a client and a server. It looks like a python dictionary but follows
# strict rules. JSON is commonly used in APIs and Web Applications because it is straightforward to read and transfer. JSON stands for JavaScript Object Notation
# because it was originally derived from JavaScript's object literal syntax. However, despite its name, JSON is a language independent data format
#  now widely used in many programming languages including Python, Java, C# and more etc. Even though JSON has JavaScript in its name, it has
# become a universal format for data exchange across different programming languages.


#                               Working with JSON in Python
#  - Python provides a Builtin JSON model to handle JSON data.
# JSON models include:
# * JSON.dumps(): This converts python object to JSON strings.
# * JSON.dump(): This writes JSON data to a file.
# * JSON.loads(): This converts JSON strings to python object.
# * JSON.load(): This reads JSON data from a file.


#                              Differences between JSON and Python dictionaries
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#       Feature     |                                 JSON                               |                   Dictionary
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Definition        | A lightweight text-based data format for exchanging data          | A built-in python data structure (mutable key-value pairs)
#---------------------------------------- -------------------------------------------------------------------------------------------------------------
# Data Type         | Always a string when stored in a file or sent over a network       | Python object (can store different types of values)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Key               | Always strings                                                     | Can be strings, numbers or tuples
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Values            | Strings, numbers, booleans, arrays, objects                        | Any Python object (lists, functions, objects, etc.)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Syntax Format     | Using double quotes " " for keys & strings                         | Uses single or double quotes  ' ' or " "
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Comments          | ❌ Not allowed                                                     | ✅ Allowed
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Trailing Commas   | ❌ Not allowed                                                     | ✅ Allowed
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Data Storage      | Stored as a text string                                            | Stored as a python object in memory
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#                           What are APIs
# An API stands for Application Programming Interface. It allows programs to communicate with each other

#                           Introduction to SOA (Service Oriented Architecture)
# SOA is a designed pattern where applications communicate through services (APIs). Each service is independent and reusable. SOA typically uses
# HTTP, SOAP or REST for communication.

#                           Why SOA
# * It is scalable and modular.
# * It allows different applications to communicate.
# * It supports interoperability across languages.
#                           Types of APIs in SOA
# * SOAP: Soap means SIMPLE OBJECT ACCESS PROTOCOL. It is xml-based and heavy.
# * REST: Rest means REPRESENTATIONAL STATE TRANSFER. It is JSON-based and lightweight. It is also the most common.
# * Graph QL: It is a flexible query-based API.
#                           Understanding Restful APIs
# - APIs follows a REST architecture where you can:
# * GET: This is to retrieve data.
# * POST: This is to send data. For example, Create a new user.
# * PUT: This is to update an existing user.
# * DELETE: This is to remove data.

import json

# Example of a JSON
var = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "subjects": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

# Dictionary
dictionary = {
    'name': 'Alice',    # Can use single quotes
    "age": 25,          # Can use double quotes
    "city": "New York",
    1: "one",           # Can use a different data type as a key
    (3, 4): "Tuple"     # JSON does NOT support tuple keys
}



# Converting Python Dictionary to JSON (json.dumps())
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_data = json.dumps(data) # Convert dictionary to JSON string
print(json_data)    # Output: {"name": "Alice", "age": 25, "city": "New York"}


# Converting JSON to Python Dictionary (json.loads())
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
python_dict = json.loads(json_string) # Convert JSON string to dictionary
print(python_dict["name"])  # Output: Alice


# Reading JSON from a File (json.load()) - If JSON is stored in a file, we can read it like this:
#with open("data.json", "r") as file:
#   data = json.load(file) #Load JSON from file
# print(data)

#Writing JSON to a file (json.dump())
data2 = {
    "name": "Bob",
    "age": 30,
    "city": "London"
}

with open("data.json", "w") as file:
    json.dump(data2, file, indent=4)    # Write JSON to file with indentation.

# Formatting JSON for Readability (indent, sort_keys).The indent=4 makes the JSON readable.
#The sort_keys = True sorts JSON keys alphabeticalLLY
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)
