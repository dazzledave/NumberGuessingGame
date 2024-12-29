import random

def number_guessing_game():
  """Plays a number guessing game with the user."""

  secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
  attempts = 0

  print("I'm thinking of a number between 1 and 100.")

  while True:
    try:
      guess = int(input("Take a guess: "))
      attempts += 1

      if guess < secret_number:
        print("Too low! Try again.")
      elif guess > secret_number:
        print("Too high! Try again.")
      else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  number_guessing_game()