import random

print("""Welcome to the game of Hangman. I hope you enjoy the game!
Currently the words you will have to guess is covered computer topic""")

# Just a list of words
def word_list():
    words = ["python", "programming", "internet", "debug", "error", "code editor", "console", "protocol", "syntax"]
    return random.choice(words)

def game(word, num_of_guesses, guess):
    status = ""
    correct_guess = 0
    for letter in word:
        if letter in num_of_guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            correct_guess += 1

    if correct_guess > 1:
        print ("Yes! The word contains " + str(correct_guess) + "'" + guess + "'" + "s")
    elif correct_guess == 1:
        print ("Yes! The word contains the letter'" + guess + "'")
    else:
        print ("No! The word does not contain the letter'" + guess + "'")

    return status


def main():
    word = word_list()
    num_of_guesses = []
    answer = False
    print ("The word contains",len(word), "letters.")
    while not answer:
        text = ("Please enter one letter or a {} - letter word.").format(len(word))
        guess = input(text)

        if guess in num_of_guesses:
            print("You've already guessed the letter '" + guess + '"')
        elif len(guess) == len(word):
            num_of_guesses.append(guess)
            if guess == word:
                answer = True
            else:
                print("That is incorrect!")
        elif len(guess) == 1:
            num_of_guesses.append(guess)
            result = game(word, num_of_guesses, guess)
            if result == word:
                answer = True
            else:
                print(result)
        else:
            print("Invalid Entry")

    print("The word is " + word + "! You got it in", len(num_of_guesses),"tries.")

main()
