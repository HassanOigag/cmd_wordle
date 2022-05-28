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

def print_keyboard(letters, type):
    #0 for wrong which mean print keyboard letter in red
    #1 for available letters which mean print available letters in blue
    if type == 0:
        print("used letters :", end=" ")
    else:
        print("available letters :", end=" ")
    for letter in letters:
        print(f"[{color_letter(letter, Fore.RED)  if type == 0 else color_letter(letter, Fore.BLUE)}]", end=" ")
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

def get_available_letters(wrong_letters):
    available_letters = []
    for letter in alpha:
        if letter not in wrong_letters:
            available_letters.append(letter)
    return available_letters

def play_wordle(words, word):
    word_length = len(word)
    attempts = 0
    guessing_board = [" "*word_length for i in range(5)]
    guesses = []
    alphabets = alpha
    wrong_letters = []
    print_board(guessing_board, word)
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
        else:
            wrong_letters  = list(set(wrong_letters + get_wrong_letters(word, guess)))
            guessing_board[attempts] = guess
            print_board(guessing_board, word)
            if guess != word:
                print_keyboard(wrong_letters, 0)
                print_keyboard(get_available_letters(wrong_letters), 1)
                guesses.append(guess)
            else:
                return True
            attempts += 1
    return False
