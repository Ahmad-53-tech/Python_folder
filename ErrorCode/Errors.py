import random
from random import randint

from ErrorCode import Maths


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You have reached the last number")

my_function()


print()
# 2 - REPRODUCE THE BUG
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1,6)
print(dice_images[dice_num])



print()
# 3 - PLAY COMPUTER
year = int(input("Enter your year of birth? "))

if 1980 < year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("")



def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = Maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])



