import random

while True:
    guesses_left = 3
    random_number = random.randint(1,10)

    while guesses_left != 0:
        print("Guess a number between 1 and 10")
        guessed_number = int(input('> '))

        if guessed_number > 0 and guessed_number < 11:
            if guessed_number < random_number:
                print("Your guess is to low")
                guesses_left -= 1
                print(guesses_left, 'tries left')
            elif guessed_number > random_number:
                print("Your guess is to high")
                guesses_left -= 1
                print(guesses_left, 'tries left')
            else:
                print("You guessed the correct number")
                random_number = random.randint(1,10)
                guesses_left = 3
        else:
            print("Please guess between 1 and 10")
    
    print("Game Over!")
    break