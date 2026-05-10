import random

print("=" * 40)
print("   Welcome to Guess the Number!")
print("=" * 40)
print()

secret = random.randint(1, 20)
tries = 0
max_tries = 4

print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_tries} tries. Good luck!")
print()

while tries < max_tries:
    tries = tries + 1
    print(f"Try {tries} of {max_tries}:")

    try:
        guess = round(float(input("Your guess: ")))
    except ValueError:
        print("Please type a number!")
        tries = tries - 1
        continue

    if guess == secret:
        print()
        print(f"*** YOU WIN! *** The number was {secret}!")
        print(f"You got it in {tries} tries!")
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")
    print()

else:
    print(f"Game over! The secret number was {secret}.")
    print("Better luck next time!")

print()
input("Press Enter to quit...")
