import sys, getopt


class WordSearch:
    """WordSearch version of the game"""

    words = None
    letter_set = ''
    filter = ''


    def __init__(self, words):
        self.words = words
    

    # resets the internal game state
    def reset(self, letter_set):
        self.letter_set = letter_set


    # processes the filter and displays the results
    def process(self):
        filter = ''
        letter_set = self.get_letter_set()
        while True:
            filter = input("Filter: ").casefold()
            if filter == '':
                letter_set = self.get_letter_set()
                continue

            # play the game
            filtered_words = self.get_words(self.words, filter)
            words_in_set = self.filter_set(filtered_words, letter_set)

            if len(words_in_set) > 0:
                print(f'All the words matching {filter} with the letter set {letter_set} using an exclusive filter')
                self.print_words(words_in_set)
            else:
                print("No matches found")
            print()


    # matches a word to the filter
    def match_word(self, word, filter):
        if len(word) != len(filter):
            print(f'Error: word {word} is different length than filter {filter}')
            exit()

        for i in range(len(word)):
            if filter[i] == '#':
                continue
            if word[i] != filter[i]:
                return

        return word


    # returns the word if it contains all the letters in the set
    def contains_set(self, word, set):
        matches = 0
        for w in word:
            if set.find(w) < 0:
                break

            matches += 1

            set = set.replace(w, '', 1)
            if len(set) == 0:
                break
        
        # only return the word if the number of matches is the same
        if matches == len(word):
            return word


    # filters a list of words based
    # filter format is:
    #     #: for placeholder
    #   A-Z: matching letters
    def filter_words(self, words, filter):
        results = []
        length = len(filter)
        for word in words:
            if len(word) != length:
                continue
            
            if self.match_word(word, filter):
                results.append(word)

        return results


    # filters a list of words based on all possible letters
    def filter_set(self, words, set):
        results = []
        for word in words:
            if self.contains_set(word, set):
                results.append(word)

        return results


    # gets all the words of the specified length
    def get_words(self, words, filter):
        results = []
        length = len(filter)
        for word in words:
            if len(word) != length:
                continue
            
            if self.match_word(word, filter):
                results.append(word)
        
        return results


    # prints the words in a set of column
    def print_words(self, words):
        for idx in range(len(words)):
            print(f" {words[idx]:<11}", end="")

            if (idx+1) % 4 == 0:
                print()

    # gets the letter set with a standard prompt
    def get_letter_set(self):
        letter_set = input("Letter set: ")
        if letter_set == '':
            exit()
        return letter_set

