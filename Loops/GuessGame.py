#1.
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
         print("You won!")
         break
else:
    print("Sorry, You failed")  



#2.
import random
secret_number = random.randint(1, 10)


guess = 0

while guess != secret_number:
    guess  = int(input("Guess a number between 1 and 10: "))
    if guess < secret_number:
        print("Too low! try again")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right!")

