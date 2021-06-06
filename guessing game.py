print("Guess who am i: what has 2 hands but no arms and legs?")

secret_word = "clock"
guess = ""
guess_count = 0
chances = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < chances:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("LOL! you loose")

else:
    print("YE! You won")