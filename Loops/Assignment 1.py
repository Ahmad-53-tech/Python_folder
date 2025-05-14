# Build a guessing game (3 trials)
print("Welcome to Ahmad's Guessing Game!")
print("I have chosen a number between 1 and 10. You have 3 attempts to guess it right!")

right_guess = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess > right_guess:
        print("Too high")
    elif guess < right_guess:
        print("Too low")
    elif guess == right_guess:
        print("You Nailed it 🎯")
        break


else:
    print("Oops! You are out of guesses")


              

    
      




