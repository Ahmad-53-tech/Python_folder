# - An Array is a data structure used to store multiple values of the same data type in a single variable.
# Python does not have a built-in support for arrays like in other languages, but if you need an array that stores elements of the same type, use the array module i.e.,
# importing an array.


#                           Some Methods in Array
# * buffer_info(): returns two values which is the array's address and size.
# * typecode: returns the typecode of an array.





from array import *
vals = array('i',[1,2,3,4,5,6,7,8,9]) # using the smaller "i" means that negative int values are allowed.

print(vals)
print(vals.buffer_info())
print(f"Typecode: {vals.typecode}")

new_arr = array(vals.typecode, (a*a for a in vals))
print(new_arr)
