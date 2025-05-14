# . Tuples
#a. Create a tuple of five different numbers and:
# * Find the length of the tuple.
# * Access the third element in the tuple.
# * Convert the tuple into a list.
#b. Given the tuple colors = ("red", "blue", "green", "yellow", "black") perform the following:
# * Print only the last two colors.
# * Check if "purple" is in the tuple.
# * Try Modifying "blue" to "cyan" and observe what happens.
my_tuple = (2, 11, 5, 20, 15)
print(f"Tuple Length: {len(my_tuple)}")
print(f"Third Element: {my_tuple[2]}")
conversion = list(my_tuple)
print(f"Conversion of tuple to list: {conversion}")
colors = ("red", "blue", "green", "yellow", "black")
print(f"Last two colors: {colors[3:]}")
if "purple" in colors:
    print("Purple is in colors")
else:
    print("Purple not in colors")
# When I tried modifying "blue" to "cyan," I received an error message saying: TypeError: 'tuple' object does not support item assignment


