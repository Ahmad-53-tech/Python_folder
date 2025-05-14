from functools import reduce
f = lambda a: a*a

result = f(5)



nums = [2, 4, 7, 8, 10, 12, 53]

evens = list(filter(lambda n: n%2 == 0, nums))
print(f"Even numbers in list: {evens}")

doubles = list(map(lambda n: n*2, evens))
print(f"Doubles of the even numbers: {doubles}")

sum = reduce(lambda a,b: a+b, doubles)
print(f"Sum of the doubled numbers: {sum}")

















