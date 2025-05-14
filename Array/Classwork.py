from array import *
arr = array('i', [])

n = int(input("Enter the length of the array: "))
for e in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search: "))
k = 0
for d in arr:
    if d == val:
        print(f"Index of val: {k}")
    k += 1