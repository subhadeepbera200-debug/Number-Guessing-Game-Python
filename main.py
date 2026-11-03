import random

def number_guessing_game():
    print("=== NUMBER GUESSING GAME ===")
    print("Welcome to Number Guessing Challenge!")
    secret_number = random.randint(1, 100)
    print("Ami 1-100 er moddhe ekta number bhebechi.")
    print("Tomar kache 5 ta chance ache!\n")

    attempts = 5
    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}/{attempts} - Tomar guess: "))
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! Tumi {i+1} barei pere gecho!")
                print(f"Secret number chilo: {secret_number}")
                break
            elif guess < secret_number:
                print("Hint: Aro BORO number bolo ⬆️\n")
            else:
                print("Hint: Aro CHOTO number bolo ⬇️\n")
        except ValueError:
            print("Please sudhu number input dao!\n")
    else:
        print(f"\n😢 Game Over! Tumi paroni.")
        print(f"Secret number chilo: {secret_number}")

if __name__ == "__main__":
    number_guessing_game()
