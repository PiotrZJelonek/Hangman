'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
import numpy as np # required for type hints: -> None

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        word = random.choice(word_list)
        s = ''
        for i in range(len(word)):
            s += '_'
        word_guessed = list(s)
        num_letters = len(set(list(word)))

        print(f"The mistery word has {num_letters} characters")
        print(word_guessed)

        self.num_letters = num_letters
        self.num_lives = num_lives
        self.list_letters = []
        self.word_guessed = word_guessed
        self.word = word

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        

        word = self.word
        word_guessed = self.word_guessed

        list_letters = self.list_letters

        list_letters.append(letter)

        # convert word to a list
        word_list = list(word) 
        
        # check if letter in word
        if letter in word_list:

            # update: a list of guessed letters,  a number of UNIQUE letters
            
            self.num_letters -= 1

            # replace dashes with a correct letter
            for i in range(len(word_list)):
                if word_list[i] == letter:
                    word_guessed[i] = letter

            # update attributes
            self.list_letters = list_letters
            self.word_guessed = word_guessed

            # print outputs
            print(self.word_guessed)
            print(f"Nice! {letter} is in the word!")

        else: 

            self.num_lives -= 1

            # print outputs
            print(self.word_guessed)
            print(f"Your guess {letter} was incorrect. You have {self.num_lives} lives left")


        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        
        need_letter = True

        while need_letter:

            letter = input("Enter a single character: ").lower()

            if letter in self.list_letters:

                print(f"{letter} was already tried")

            else:

                n = len(letter) 

                if n > 1:
                    print("Please, enter just one character")
                elif n < 1:
                    print("Please enter a character")
                elif n == 1:
                    # print("That\'s right")
                    self.check_letter(letter)
                    need_letter = False

        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)

    game_stops = False
    while not game_stops:
        game.ask_letter()
        game_stops = (game.num_lives == 0) or (game.num_letters == 0)

    if game.num_letters == 0:
        print("Congratulations! You won!")
    elif game.num_lives == 0:
        print(f"You lost! The word was {game.word}")
    


    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
