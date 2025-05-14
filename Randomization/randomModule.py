import random

#This will produce a random whole number between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# random.random() generates a random floating point number between 0.0(inclusive) and 1.0 (exclusive) like 0.0 <= random.random() < 1.0
# Will generate a random number between 0.0 and 10.0 (10.0 exclusive and 0.0,inclusive)
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# This will generate a random floating point number 1.0 and 10.0 like a <= random.uniform(a,b) <= b (both a and b inclusive).
random_float = random.uniform(1, 10)
print(random_float)

# random.randint(0, 1) will only return either 0 or 1 (never a decimal)
# random.randint(a, b) returns a random integer in the range (a, b), including both a and b.
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
