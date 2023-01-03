# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list = list(secret_word)
    delete_guessed_letter = list(
        filter(lambda character: character not in letters_guessed, secret_word_list))
    return len(delete_guessed_letter) == 0


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_"
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            result += letter
    return result


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.strip()
    other_word = other_word.strip()

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in my_word:
                return False
            continue

        if my_word[i] != other_word[i]:
            return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            result.append(word)
    print(" ".join(result))
    return result


def is_input_valid(user_input):
    user_input = str.lower(user_input)
    return len(user_input) == 1 and str.isalpha(user_input)


def is_input_hint(user_input):
    return user_input == "*"


def get_score(secret_word, guess_left):
    return len(tuple(list(secret_word))) * guess_left


def print_hline():
    print("-"*13)


def game_start(game_state):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        len(game_state["secret_word"])))
    print_hline()


def is_game_end(game_state):
    return is_word_guessed(game_state["secret_word"], game_state["letters_guessed"]) or game_state["guess_left"] == 0


def round_start(game_state):
    print("You have {} guesses left.".format(game_state["guess_left"]))
    print("Available letters: {}".format(
        get_available_letters(game_state["letters_guessed"])))

# return True if warning is subtracted, return False if guess is subtracted


def subtract_warning(game_state) -> bool:
    if game_state["warning_left"] != 0:
        game_state["warning_left"] -= 1
        return True
    else:
        game_state["guess_left"] -= 1
        return False


def penalize_invalid_input(game_state):
    if subtract_warning(game_state):
        print("Oops! That is not a valid letter. You have {} warnings left: {}".format(
            game_state["warning_left"], get_guessed_word(game_state["secret_word"], game_state["letters_guessed"])))
    else:
        print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: {}".format(
            get_guessed_word(game_state["secret_word"], game_state["letters_guessed"])))


# get_input would store the user's input if it's a char and return True; else it would return False
def get_input(game_state):
    user_input = input("Please guess a letter: ").strip()

    if is_input_hint(user_input):
        print("Possible word matches are: ")
        show_possible_matches(get_guessed_word(
            game_state["secret_word"], game_state["letters_guessed"]))
        return False

    if not is_input_valid(user_input):
        penalize_invalid_input(game_state)
        return False

    game_state["user_input"] = user_input
    return True


def is_letter_guessed(game_state):
    if game_state["user_input"] in game_state["letters_guessed"]:
        if subtract_warning(game_state):
            print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(
                game_state["warning_left"], get_guessed_word(game_state["secret_word"], game_state["letters_guessed"])))
        else:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(
                get_guessed_word(game_state["secret_word"], game_state["letters_guessed"])))
        return True
    else:
        return False


def penalize_wrong_guess(game_state):
    vowels = "aeiou"
    if game_state["user_input"] in vowels:
        game_state["guess_left"] -= 2
    else:
        game_state["guess_left"] -= 1


def check_guess(game_state):
    user_input = game_state["user_input"]

    game_state["letters_guessed"].append(user_input)

    if user_input in game_state["secret_word"]:
        print("Good guess: {}".format(get_guessed_word(
            game_state["secret_word"], game_state["letters_guessed"])))
    else:
        penalize_wrong_guess(game_state)
        print("Oops! The letter is not in my word: {}".format(
            get_guessed_word(game_state["secret_word"], game_state["letters_guessed"])))


def round_main(game_state):
    if not get_input(game_state):
        return
    if is_letter_guessed(game_state):
        return
    check_guess(game_state)


def round_end(game_state):
    print_hline()


def game_main(game_state):

    round_start(game_state)
    round_main(game_state)
    round_end(game_state)


def game_end(game_state):
    if is_word_guessed(game_state["secret_word"], game_state["letters_guessed"]):
        print("Congratulations, you won!")
        print("Your total score is for this game is: {}".format(
            get_score(game_state["secret_word"], game_state["guess_left"])))
    else:
        print("Sorry, you ran out of guesses. The word is {}".format(
            game_state["secret_word"]))


def hangman(secret_word, enable_hint=False):
    # Init game_state
    game_state = {"guess_left": 6,
                  "warning_left": 3,
                  "letters_guessed": [],
                  "secret_word": secret_word,
                  "user_input": "",
                  "enable_hint": enable_hint
                  }
    game_start(game_state)

    while not is_game_end(game_state):
        game_main(game_state)

    game_end(game_state)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hangman(secret_word, enable_hint=True)

def print_name():
    print(f"__name__ = {__name__}")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
