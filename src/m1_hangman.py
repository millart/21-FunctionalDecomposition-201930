"""
Hangman.

Authors: Maria Bruner and Emily Millard.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    print('Welcome to the game of hangman! To start things off:')
    word = pick_word()
    allowed = pick_guesses()
    repeat(word, allowed)
    play_again()


def pick_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        minimum_length = int(input('What minimum length do you want for the secret word?'))
        while True:
            r = random.randrange(0, len(words))
            if len(words[r]) >= minimum_length:
                return words[r]


def pick_guesses():
    allowed = int(input('How many unsuccessful choices do you want to allow yourself?'))
    return allowed


def get_guess():
    guess = input('What letter do you want to try?')
    return guess


def find_letter(word, letter):
    indices = []
    for k in range(len(word)):
        if word[k] == letter:
            indices.append(k)

    return indices


def new_result(total_guess, new_guess, letter):
    good_guess = 0
    if len(new_guess) > 0:
        good_guess = 1
        for k in range(len(new_guess)):
            index = new_guess[k]
            total_guess[index] = letter
        return total_guess, good_guess
    else:
        return total_guess, good_guess


def print_result(good_guess, letter, word, total_guess, allowed):
    string = ''
    for k in range(len(total_guess)):
        string = string + str(total_guess[k])
    if good_guess == 1:
        if string == word:
            print('You won! The secret word is:', word)
        else:
            print('Good guess!')
            print('Here is what you currently know about the secret word:')
            print(string)
            return allowed
    else:
        allowed = allowed - 1
        print('Sorry! There are no', letter, 'letters in the secret word. You still have', allowed,
              'unsuccessful guesses left before you lose the game!')
        print('Here is what you currently know about the secret word:')
        print(string)
        if allowed == 0:
            print('You lose! The secret word was:', word)
        return allowed


def repeat(word, allowed):
    total = 0
    current_guesses = []
    for k in range(len(word)):
        current_guesses.append('-')
    while True:
        letter = get_guess()
        indices = find_letter(word, letter)
        current_guesses, good_guess = new_result(current_guesses, indices, letter)
        allowed = print_result(good_guess, letter, word, current_guesses, allowed)
        if allowed == 0:
            break
        total = total + len(indices)
        if total == len(word):
            break


def play_again():
    answer = input('Play another game? (y/n)')
    if answer == 'y':
        main()


main()
