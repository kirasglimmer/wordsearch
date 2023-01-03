from abc import ABC, abstractmethod

class WordGame(ABC):

    words = []


    # constructor
    def __init__(self, words):
        print(f'Game initialized with {len(words)} words')
        self.words = words


    # run the game
    @abstractmethod
    def process(self):
        pass


    # reset to initial game state
    @abstractmethod
    def reset(self):
        pass


    # matches a word to the filter
    def match_word(self, word, filter):
        # skip words that aren't the same length as the filter
        if len(word) != len(filter):
            return None

        # find word based on filter (# skips, letter matches)
        for i in range(len(word)):
            if filter[i] == '#':
                continue
            if word[i] != filter[i]:
                return

        return word


    # filters a list of words
    # filter format is:
    #     #: for placeholder
    #   A-Z: matching letters
    def filter_words(self, words, filter):
        results = []
        for word in words:
            if self.match_word(word, filter):
                results.append(word)

        return results.sort()


    # gets all the words of the specified length
    def get_words_of_length(self, words, word_length):
        results = []
        for word in words:
            if len(word) != word_length:
                continue
            
            results.append(word.casefold())

        return results


    # Filters the word list based on whether or not the letters in the list are included
    def filter_words_by_letters(self, words, letters, included):
        results = []
        for word in words:
            skip = False
            for letter in letters:
                position = word.find(letter)
                if included == True and position < 0:
                    skip = True
                    continue
                elif included == False and position > -1:
                    skip = True
                    continue

            if skip:
                continue

            results.append(word)
        
        return results


    # prints the words in a set of column
    def print_words(self, words):
        if len(words) > 0:
            print(f'Matching words')

            for idx in range(len(words)):
                print(f" {words[idx]:<11}", end="")

                if (idx+1) % 8 == 0:
                    print()
        else:
            print("No matches found")
        print()
        