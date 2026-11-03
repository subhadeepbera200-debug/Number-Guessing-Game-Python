import random

def number_guessing_game():
    print("NUMBER GUESSING GAME")
    print("I have selected a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try a higher number.")
            elif guess > secret_number:
                print("Too High! Try a lower number.")
            else:
                print(f"Congratulations! You won in {attempts} attempts!")
                print(f"The secret number was {secret_number}")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
