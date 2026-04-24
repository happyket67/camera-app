```python
import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("Choose difficulty:")
    print("1. Easy (1–10, 5 tries)")
    print("2. Medium (1–50, 7 tries)")
    print("3. Hard (1–100, 10 tries)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        max_num = 10
        attempts = 5
    elif choice == "2":
        max_num = 50
        attempts = 7
    elif choice == "3":
        max_num = 100
        attempts = 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        max_num = 10
        attempts = 5

    secret_number = random.randint(1, max_num)
    score = attempts * 10

    print(f"\nI'm thinking of a number between 1 and {max_num}...")

    while attempts > 0:
        try:
            guess = int(input(f"Attempts left ({attempts}): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if guess == secret_number:
            print(f"🎉 Correct! You win! Final score: {score}")
            return
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        attempts -= 1
        score -= 10

    print(f"💀 You lost! The number was {secret_number}")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
```
