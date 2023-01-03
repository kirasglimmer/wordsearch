from src.wordgame import WordGame


# Wordle starts out with a board of 5 columns for letters, and
# 6 rows for words
# The player guesses the word, and the filtering starts to happen
# based on known invalid letters, valid letters, and valid letters
# with a known position
# filter is done by excluding letters first, excluding words that
# don't have letters in the correct position, and then excluding
# words that don't have any of the known good letters

class Wordle(WordGame):
    """Processes hints for the Wordle game"""

    words = []
    word_list = []  # the set of possible matches


    def __init__(self, words):
        self.words = words
        self.reset()


    # resets the game state
    def reset(self):
        self.letter_set = 'abcdefghijklmnopqrstuvwyxz'
        self.base_words = super().get_words_of_length(self.words, 5)
        print(f'There are {len(self.base_words)} words with length 5 to search within')


    # gets a unique letter set from the given list
    def unique_letters(self, letters):
        return ''.join(set(letters))


    # process the game
    def process(self):
        print('Wordle, the crazy 5 letter word guessing game')
        print('  invalid letters: all the letters not in the guess word')
        print('    known letters: all the known letters but unknown position')
        print('    valid letters: the letters who''s exact position is known')
        print()

        while True:
            bad_letters   = self.unique_letters(input('Invalid letters: ') or '')
            if not bad_letters:
                break

            known_letters = input('  Known letters: ') or ''
            valid_letters = input('  Valid letters: ') or '#####'

            print(f'Finding words that exclude {bad_letters}, contain {known_letters}, and match the exact letters with {valid_letters}')

            filtered_words = self.filter_words_by_letters(self.base_words, bad_letters, False)
            filtered_words = self.filter_words_by_letters(filtered_words, known_letters, True)
            filtered_words = super().filter_words(filtered_words, valid_letters)
            super().print_words(filtered_words)
