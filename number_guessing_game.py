import random
import os

game_going = True

print('Welcome to the number guessing game.')

while game_going:
    num_to_guess = random.randint(1, 100)
    diff = input('Choose difficulty level, "easy" or "hard": ').lower()
    while diff not in ('easy', 'hard'):
        diff = input('Invalid input. Please choose "easy" or "hard": ').lower()
    if diff == 'easy':
        attempts = 10
    else:
        attempts = 5

    os.system('clear')
    print(f'{diff.title()} mode selected. {attempts} attempts allowed.')
    
    while attempts > 0:
        try:
            user_input_num = int(input('Guess a number between 1 and 100: '))
        except:
            print('Invalid input. Please enter an integer.')
            continue
        if user_input_num not in range(101):
            print('Invalid input. Number is between 1 and 100.')
        elif user_input_num == num_to_guess:
            print(f"{user_input_num} was correct. You win.")
            break
        elif user_input_num > num_to_guess:
            attempts -= 1
            print(f'{user_input_num} was too high. {attempts} attempts remaining.')
        elif user_input_num < num_to_guess:
            attempts -= 1
            print(f'{user_input_num} was too low. {attempts} attempts remaining.')
        else:
            print('Invalid input.')
    
    if attempts == 0:
        print(f'Ran out of attempts. Correct number was {num_to_guess}.')

    play_another = input('Play again? Y or N: ').lower()
    if play_another == 'n':
        game_going = False
    else:
        os.system('clear')

print('Goodbye')
        