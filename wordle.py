import pyfiglet as pf
from string import ascii_lowercase as alpha
from colorama import Fore, Style
import random


def print_border(word_length):
    for i in range(word_length):
        print("-----", end=" ")
    print()


def print_word(word, guess):
    print_border(len(guess))
    status = check_guess(word, guess)
    for index, letter in enumerate(guess):
        if status[index][letter] == 1:
            print(f"| {Fore.GREEN}{letter}{Style.RESET_ALL} |", end=" ")
        elif status[index][letter] == 2:
            print(f"| {Fore.YELLOW}{letter}{Style.RESET_ALL} |", end=" ")
        else:
            print(f"| {Fore.RED}{letter}{Style.RESET_ALL} |", end=" ")
    print()
    print_border(len(guess))


def print_board(guess_board, word):
    for guess in guess_board:
        print_word(word, guess)
        print()


def check_guess(word, guess):
    status = []
    for index, letter in enumerate(guess):
        if letter in word:
            if guess[index] == word[index]:
                # 1 means the letter is in the word and its correct spot
                status.append({letter : 1})
            else:
                # 2 means the letter is in the word but in a wrong spot
                status.append({letter : 2})
        else:
            status.append({letter : 0})  # 0 means the letter is not in the actual word
    return status

def get_word():
    with open("words","r") as file:
        words = file.readlines()
        words = [word[0:-1] for word in words]
        word = random.choice(words)
    return [words, word]
if __name__ == "__main__":
    title = pf.figlet_format("WORDLE")
    print(title)
    words, word = get_word()
    word_length = len(word)
    attempts = 0
    guesses = [" "*word_length for i in range(5)]
    wrong_letters = []
    print_board(guesses, word)
    won = False
    while attempts < word_length:
        guess = input("Guess the word: > ")
        if len(guess) != word_length:
            print("Please, your guess word should be of length 5")
        elif not guess.isalpha():
            print("Please, your should only contains alphabetic characters")
        elif guess.isupper():
            print("Please, only lowercase characters are accepted")
        elif guess not in words:
            print("word doesn't exist in the list")
        else:
            guesses[attempts] = guess
            print_board(guesses, word)
            if guess == word:
                won = True
                break
            attempts += 1

    if won:
    	message = pf.figlet_format("Well Done!")
    	print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    else:
        message  = pf.figlet_format("Good luck next time!")
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")
