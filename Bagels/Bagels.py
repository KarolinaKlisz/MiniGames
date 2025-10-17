import random as rd

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():

    print("Bagels, a logical deduction game. \n")
    print("Author: Karolina \n")
    print("I'm thinking of a 3-digit number with no repeating digits. Try to guess it. Here are the clues: \n")
    print("1. Pico - one digit is correct but in the wrong position. \n")
    print("2. Fermi - one digit is correct and in the correct position. \n")
    print("3. Bagels - no digit is correct. \n")

    while True:
        sec_num = secret_number()
        print(f"I've chosen a number! You have {MAX_GUESSES} attempts to guess it. Good luck!")
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Attempt #", numGuesses)
                guess = input("> ")
            clues = get_clues(guess, sec_num)
            print(clues)
            numGuesses += 1

            if guess == sec_num:
                break
            if numGuesses > MAX_GUESSES:
                print("Too many guesses, try again.")
                print("The correct answer is: ", sec_num)

        print("Wanna play again? (yes / no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thank you for playing!")


def secret_number():
    list_of_numbers = [x for x in range(0,10)]
    rd.shuffle(list_of_numbers)
    sec_num = ""
    for i in range(NUM_DIGITS):
        sec_num += str(list_of_numbers[i])

    return sec_num

def get_clues(guess, sec_num):
    if guess == sec_num:
        return "Congratulations, you guessed it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == sec_num[i]:
            clues.append("Fermi")
        elif guess[i] in sec_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ','.join(clues)


if __name__ == "__main__":
    main()