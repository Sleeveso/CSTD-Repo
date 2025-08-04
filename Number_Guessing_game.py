import random as rd
print("************************************")
print("Welcome to the Number Guessing Game!")
print("************************************")
print("///////////////////////////////////////////////////////////")
print("                            RULES                          ")
print("///////////////////////////////////////////////////////////")
print("You have a limit of five guesses.")
print("You are allowed to choose the range of the number to guess.")
print("///////////////////////////////////////////////////////////")


name = input("Please enter your name: ")
lowest_number = int(input(f"{name} Enter the lowest number: "))
highest_number = int(input("Enter the highest number: "))


no_of_guess = 0
score = 0
times_played = 0
is_running = True
answer = rd.randint(lowest_number, highest_number)

print(f"\nGuess a number between {lowest_number} and {highest_number}")

while is_running:
    guess = int(input("Enter a guess: "))
    no_of_guess += 1

    if guess < lowest_number or guess > highest_number:
        print("The number you chose is out of range.")
        print(f"Please enter a number from {lowest_number} to {highest_number}")
        continue

    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Correct! You win!")
        print(f"Number of guesses: {no_of_guess}")
        score += 1

        play_again = input("Press 'y' to play again or any other key to quit: ").lower()
        if play_again == "y":
            no_of_guess = 0
            times_played += 1
            answer = rd.randint(lowest_number, highest_number)
            print(f"\nNew game! Guess a number between {lowest_number} and {highest_number}")
            continue
        else:
            print(f"Username: {name}")
            print(f"\nYou played {times_played + 1} game(s), and your overall score is: {score}")
            break

    if no_of_guess >= 5:
        print("\nYou lose!!")
        print(f"You used {no_of_guess} out of 5 guesses.")
        print(f"The correct answer was: {answer}")
        play_again = input("Press 'y' to play again or any other key to quit: ").lower()
        if play_again == "y":
            no_of_guess = 0
            times_played += 1
            answer = rd.randint(lowest_number, highest_number)
            print(f"\nNew game! Guess a number between {lowest_number} and {highest_number}")
        else:
            print(f"Username: {name}")
            print(f"\nYou played {times_played + 1} game(s), and your overall score is: {score}")
            is_running = False

    
    
    
    
    
   
    
    
   