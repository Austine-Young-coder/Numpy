import random

print("🎮 Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 50.")
print("You have 7 attempts.\n")

secret_number = random.randint(1, 50)
attempts = 7

while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))
    except:
        print("❌ Please enter a valid number.\n")
        continue

    if guess < secret_number:
        print("📉 Too low!\n")
    elif guess > secret_number:
        print("📈 Too high!\n")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        break

    attempts -= 1
    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print(f"💀 Game Over! The number was {secret_number}.")