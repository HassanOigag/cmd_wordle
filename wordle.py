import pyfiglet as pf
from string import ascii_lowercase as alpha
from colorama import Fore, Style
import random


def print_border(word_length):
    for i in range(word_length):
        print("-----", end=" ")
    print()

def color_letter(letter, color):
    return f"{color}{letter}{Style.RESET_ALL}"

def print_word(word, guess):
    print_border(len(guess))
    status = check_guess(word, guess)
    for index, letter in enumerate(guess):
        if status[index][letter] == 1:
            print(f"| {color_letter(letter, Fore.GREEN)} |", end=" ")
        elif status[index][letter] == 2:
            print(f"| {color_letter(letter, Fore.YELLOW)} |", end=" ")
        else:
            print(f"| {color_letter(letter, Fore.RED)} |", end=" ")
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

def print_keyboard(letters):
    for letter in letters:
        print(f"[{color_letter(letter, Fore.RED)}]", end=" ")
    print()

def get_wrong_letters(word, guess):
    letters = []
    for letter in guess:
        if letter not in word:
            letters.append(letter)
    return letters

def check_for_used_letters(wrong_letters, guess):
    used_letters = []
    for letter in guess:
        if letter in wrong_letters:
            used_letters.append(letter)
    return used_letters

def wordle():
    pass
if __name__ == "__main__":
    title = pf.figlet_format("WORDLE")
    print(title)
    words, word = get_word()
    word_length = len(word)
    attempts = 0
    guessing_board = [" "*word_length for i in range(5)]
    guesses = []
    alphabets = alpha
    wrong_letters = []
    print_board(guessing_board, word)
    won = False
    while attempts < word_length:
        guess = input("Guess the word: > ")
        used_letters = check_for_used_letters(wrong_letters, guess)
        if len(guess) != word_length:
            print("Please, your guess word should be of length 5")
        elif not guess.isalpha():
            print("Please, your should only contains alphabetic characters")
        elif guess.isupper():
            print("Please, only lowercase characters are accepted")
        elif guess not in words:
            print("word doesn't exist in the list")
        elif guess in guesses:
            print("you've already guessed that")
        elif len(used_letters) != 0:
            print(f"these letters {used_letters} are already used")
        else:
            wrong_letters  = list(set(wrong_letters + get_wrong_letters(word, guess)))
            guessing_board[attempts] = guess
            print_board(guessing_board, word)
            print_keyboard(wrong_letters)
            if guess == word:
                won = True
                break
            else:
                guesses.append(guess)
            attempts += 1

    if won:
    	message = pf.figlet_format("Well Done!")
    	print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    else:
        message  = pf.figlet_format("Good luck next time!")
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")
