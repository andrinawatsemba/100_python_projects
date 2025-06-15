import random

number_to_guess = random.randint(1,10)

print('Welcome to the Number Guessing Game!')

print('Guess a number between 1 and 10')

while True:
    guess = int(input('type your guess:'))
    attempts += 1

    if guess == number_to_guess:
        print (f'Congratulations! You guessed it in {attempts} attempts')
        break
    elif guess < number_to_guess:
        print('too low. Try again')
    else:
        print('Too high. Try again.')
        