# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

import string
availableLetters = string.ascii_lowercase
availableLetters = [char for char in availableLetters]

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
# secretWord = chooseWord(wordlist).lower()
secretWord = chooseWord(wordlist).lower()
secretWordLetters = sorted([char for char in secretWord])
secretWordLetters = list(dict.fromkeys(secretWordLetters))
lettersGuessed = []
correctlyGuessedLetters = []


def isWordGuessed(secretWord, correctlyGuessedLetters):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
  '''
  # FILL IN YOUR CODE HERE...

  if sorted(correctlyGuessedLetters) == secretWordLetters:
    return True
  else:
    return False

def getGuessedWord(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
  '''
  # FILL IN YOUR CODE HERE...
  
  guessedWord = ''
  for letter in secretWord:
    if letter in lettersGuessed:
      guessedWord = guessedWord + letter + " "
    else:
      guessedWord = guessedWord + "_ "

  return guessedWord



def getAvailableLetters(lettersGuessed, typedLetter):
  '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
  # FILL IN YOUR CODE HERE...
  
  availableLetters.remove(lettersGuessed[-1])
  
  return "".join(availableLetters)

def giveInfo(typedLetter):
  print("Your guessed word so far: " + getGuessedWord(secretWord, lettersGuessed))
  print("Available letters: " + getAvailableLetters(lettersGuessed, typedLetter))
    
def hangman(secretWord):
  '''
  secretWord: string, the secret word to guess.

  Starts up an interactive game of Hangman.

  * At the start of the game, let the user know how many 
    letters the secretWord contains.

  * Ask the user to supply one guess (i.e. letter) per round.

  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.

  * After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.

  Follows the other limitations detailed in the problem write-up.
  '''
  # FILL IN YOUR CODE HERE...
  global lives
  print("Lives left:", lives)

  global first_round
  if first_round == True:
    print("The secret word has", len(secretWord), "letter(s)")
    first_round = False

  while True:
    typedLetter = input("Guess a letter: ")
    if typedLetter.isalpha() and typedLetter.islower() and len(typedLetter) == 1:
      if typedLetter not in lettersGuessed:
        lettersGuessed.append(typedLetter)
        break
      else:
        print("You have already guessed that letter.")
    else:
      print("Please guess a valid letter.")

  if typedLetter in secretWord:
    correctlyGuessedLetters.append(typedLetter)
    print("You have correctly guessed a letter!")
    if isWordGuessed(secretWord, correctlyGuessedLetters) == True:
      print("Congratulations! You've guessed the word:", secretWord, "!")
      return True
    else:
      print()
      giveInfo(typedLetter)
  else:
    lives = lives - 1
    print("You have incorrectly guessed a letter :((")
    print()
    giveInfo(typedLetter)

  print()
  return False


lives = 9
first_round = True

while True:
  if lives <= 0:
    print("Oh no! Looks like you've run out of lives.")
    print("The word is:", secretWord)
    break
  if hangman(secretWord) == True:
    break
  

