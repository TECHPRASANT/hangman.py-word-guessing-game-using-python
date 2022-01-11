# BY Prashant Bhandari

import random
import string

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]

def choose_random_word(wordlist):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
 
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    # TODO: Fill in your code here
    # prints loading word list from file:words.txt
    print(f'Loading word list from file: {WORDLIST_FILENAME}') 
    # inFile: file
    word_file = open(WORDLIST_FILENAME,"r")
    read_file = word_file.read()
    wordlist = read_file.split(" ")
    print(f"{len(wordlist)} words loaded.")
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """ 
    return wordlist
    

# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function



def is_word_guessed(word, letters_guessed):
    """
    guess: char, a letter that the user guessed
    returns: boolean, True if letter is in the word, False if letter is not
    """
    # TODO: Fill in your the code here
    is_my_word_guessed = False
    if (all(x in letters_guessed for x in list(word))):
        is_my_word_guessed = True
    return is_my_word_guessed


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here
    guessed_string = " "
    for letter in word:
        if letter.lower() in letters_guessed:
            print(letter,end="")
        else:
            print("_",end= " ")


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
    letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in letters:
            letters.remove(letter)

    print(f"Available letters: {''.join(letters)}")

    
def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    # Load the list of words into the variable wordlist
    # so that it can be accessed from anywhere in the program
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    # TODO: Fill in your code here
    while True:
        try:
            letters_guessed = []
            vowel = ["a", "e", "i", "o", "u"]
            tries = 8 # max 8 guesses applied
            score = 0 
            while tries > 0:
                print(f"You have {tries} guesses left.")
                get_remaining_letters(letters_guessed)
                guess = str(input("Please guess a letter: ")).lower()

                while guess[0] in letters_guessed:
                    '''
                    only the first letter of guess is considered
                    '''
                    print(f"Oops! You've already guessed that letter: {get_guessed_word(word, letters_guessed)}")
                    print()
                    print("-------------")
                    guess = str(input("Please guess a letter: ")).lower()

                if guess[0] not in word:
                    '''
                    if vowels are guessed wrong 2 guesses from the 
                    total guesses are deducted
                    '''
                    if guess in vowel:
                        tries = tries - 2
                    else:
                        tries = tries - 1

                letters_guessed.append(guess[0])
                if guess[0] in word:
                    print("Good guess:", end=" ")
                    get_guessed_word(word, letters_guessed)
                else:
                    print("Oops! That letter is not in my word: ", end=" ")
                    get_guessed_word(word, letters_guessed)

                print()
                print("-------------------")

                word_is_guessed_or_not = is_word_guessed(word, letters_guessed)
                if word_is_guessed_or_not == True:
                    #checks if word guessed completed or not. if completed the prompts Congratulations and shows score
                    unique_char = set(word)
                    score = tries * len(unique_char)
                    print("Congratulations, you won")
                    print(f"Your total score for this game is: {score}")
                    break
            if tries == 0:
                #if tries become too much than given 
                print(f"Sorry, you ran out of guesses. The word was: {word}")
                exit() # exit from the whole program when user ran out of guesses
            return score
        except IndexError:
            pass

def scoreboard():
    '''
     a function to print the score board
     of the first three highscorers
    :return:
    does not return anything
    '''
    try:
        file = open("scores.txt", 'r')
        readthefile = file.readlines()
        sorted_data = sorted(readthefile, reverse=True)
        print("Score       " + " Name")
        print("--------------------------")
        for line in range(3):
            print(str(sorted_data[line]))
        file.close()
    except IndexError:
        pass

def high_score():
    '''
    to find the highscore from the file
    :return:
    return list_all
    '''
    list_all = []
    with open("scores.txt", "r") as f:
        for line in f:
            list_all = line.split(" ")
    return list_all


def update_scoreboard(name,score):
    '''
    a function to update the score board

    :return:
    does not return anyvalue
    '''
    file = open("scores.txt", 'a')
    file.write("\n"+(str(score))+"          " + (name) ) # Write on the scores.txt file if user save his/her score
    print("OK, your score has been saved. ") # this prompts the succed of score saved in scores.txt
    file.close()

#this funtion  is to make decision either user want to save their obtained final score just by inputing y or n.
#the program stops only in two condition
# 1. if the user type y and save score then it calls game_decision_c function and follows the stoping condition of that function
#2. if the user type n and  doesn't save score then it calls game_decision_c function and follows the stoping condition of that function
def score_decision_controller_main():
    word = choose_random_word(wordlist)
    name = str(input("What is your name: ")) #it takes the player name as input in variable name
    highscore_list = [] 
    final_score=hangman(word) 
    #store the return score  values from hangman(word) function to variable final_score 
    # and also runs hangman(word) function
    highscore_list = high_score() #get all highscore list from highscore funtion
    if final_score !=0:
                if highscore_list[0] != "\n" and len(highscore_list) != 0:
                    if int(final_score) > int(highscore_list[0]):
                        # if current player final score is greater than in the list of all players scores list 
                        # then it prompts A new personnel best! 
                        # and give access user if they want to  save their score or not  otherwise do elif statement
                        print("A new personal best!") 
                        while True:
                            decision_save = str(input("Would you like to save your score(y/n): ")).lower()
                            if decision_save != "y" and decision_save != "n":
                                pass
                            elif decision_save == "y":
                                update_scoreboard(name, final_score) # save score in scoreboard if user type y
                                game_decision_controller_main() # calling game_decision_controller_main() function
                                break
                            elif decision_save == "n":
                                game_decision_controller_main() # calling for do the task of game_decision_controller_main() funtion if user type n
                                break
                    elif int(final_score) < int(highscore_list[0]) or int(final_score) == int(highscore_list[0]): 
                        # if current player final score is less than in the list of all player scores list 
                        # or current player final score is equal to list of all player scores 
                        # then it  gives access user if they want to save their score or not .
                        while True:
                            decision_save = str(input("Would you like to save your score(y/n): ")).lower()
                            if decision_save != "y" and decision_save != "n":
                                pass
                            elif decision_save == "y":
                                update_scoreboard(name, final_score) # save score in scoreboard if user type y
                                game_decision_controller_main() # calling game_decision_controller_main() function
                                break
                            elif decision_save == "n":
                                game_decision_controller_main() # calling for do the task of game_decision_controller_main() funtion if user type n
                                break

# -----------------------------------

#this funtion  is to control the user decision what they want either play game or see scoreboard  or quit game.
#the program stops only in two condition
# 1. if they type q for quit when related inputs prompts
# 2. If they exceed the gueses and failed in game
def game_decision_controller_main():
    what_to_do = str(input("Do you want to Play (p) view the leaderboard (l) or quit (q): ")).lower()
    if what_to_do=='p':
        score_decision_controller_main() #calling score_main funtion. this function control the score controlling process
        while True:
            what_to_do_next = str(input("Would you like to play (p) or view the leaderboard (l): ")).lower()
            if what_to_do_next=='p':
                score_decision_controller_main() #calling score_main funtion. this function control the score controlling process
            elif what_to_do_next=='l':
                scoreboard()  # callig scoreboard() funtion . this funtion shows the list of top 3 scorers.  
    elif what_to_do=='l':
        scoreboard()
        while True:
            what_to_do_next = str(input("Would you like to play (p) or view the leaderboard (l): ")).lower()
            if what_to_do_next=='p':
                score_decision_controller_main() #calling score_main funtion. this function control the score controlling process
            elif what_to_do_next=='l':
                # callig scoreboard() funtion if user type l . this funtion shows the list of top 3 scorers. 
                scoreboard()   
    elif what_to_do=='q':
        # prompts  Thanks for playing good bye and exit from the program if user type q
        print("Thanks, for playing goodbye!") 
        exit()
    
# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    wordlist = load_words() # this funtions runs first in program.
    print("Welcome to Hangman Ultimate Edition") #this prompts the welcoming message
    game_decision_controller_main() 
    
