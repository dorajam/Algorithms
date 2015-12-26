# Dora Jambor, dorajambor@gmail.com
# September 2015
# hangman.py
# Implementation of the hangman game, completed for MIT 6.00x


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for c in secretWord:
        if c in lettersGuessed:
            result = result + c 
        else:
            result = result + '_ '
    return result
    
    
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for c in secretWord:
        if c in lettersGuessed:
            pass
        else: 
            return False
    return True


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = set(alphabet)-set(lettersGuessed)
    return "".join(sorted(list(alphabet)))

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
    lettersGuessed = ''
    guess = 8 
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' %len(secretWord)
    print '----------------------'

    while isWordGuessed(secretWord, lettersGuessed) == False:
        print 'You have %i guesses left' %guess
        result = getAvailableLetters(lettersGuessed)
        print 'Available Letters:' + result
        letter = raw_input('Please guess a letter: ')
        letter = letter.lower()
        lettersGuessed = lettersGuessed + letter
        
        # FEEDBACK AFTER INPUT
        if letter not in result and letter.isalpha():
            print 'Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed)
            print '----------------------'
        elif letter in secretWord:
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            print '----------------------'
        elif letter not in secretWord:
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            print '----------------------'
            guess -= 1
            
        if guess == 0:
            break
         
    if isWordGuessed(secretWord, lettersGuessed) ==  True:
        print 'Congratulations, you won!'
    if guess == 0:
        print '	Sorry, you ran out of guesses. The word was else.'
        

hangman('dora')