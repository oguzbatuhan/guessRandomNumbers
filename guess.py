import random

#Types of challenges.
print("Welcome to the number guessing game.")
print("Choose difficulty.")
print("1. Easy (numbers 1 to 10, right to guess 3.)")
print("2. Medium (numbers 1 to 500, right to guess 6.)")
print("3. Medium (numbers from 1 to 1000, right to guess 9.)")


Difficulty = int(input("Choose difficulty (1-3): "))

# if controls.
if Difficulty == 1 :
    held = random.randint(1,10)
    print("Difficulty selected, Computer kept a number between 1 and 10.")
elif Difficulty == 2 :
    held = random.randint(1,500)
    print("Difficulty selected, Computer kept a number between 1 and 500.")
elif Difficulty == 3 :
    held = random.randint(1,1000)
    print("Difficulty selected, Computer kept a number between 1 and 1000.")
else:
    print("Invalid value.")

# RightToGuess
if Difficulty == 1 :
    rightToGuess = 3
elif Difficulty == 2 :
    rightToGuess = 6
else:
    rightToGuess = 9

# remaining guess right, veriables.
remainingGuessRight = "Remaining guess right"

# While loops.
while rightToGuess >= 0 :
    guess = int(input("Enter your prediction: "))
    if held == guess:
        print("Congratulations.")
        break
    elif held < guess:
        rightToGuess -= 1
        print("Smaller.")
        print("Right to guess", rightToGuess)
    elif held > guess:
        rightToGuess -= 1
        print("Bigger.")
        print("Right to guess", rightToGuess)
    else:
        print("Invalid value.")

    if rightToGuess == 0 :
        print("You're out of guesses. Random numeric number: ", held)
        break