from src.wordgame import WordGame
from multiprocessing import Pool, Lock

class WordSearch(WordGame):
    """WordSearch game"""

    words = []
    letter_set = ''
    pool_size = 8
    lock = Lock()


    # constructor
    def __init__(self, words):
        self.words = words


    # resets the internal game state
    def reset(self, letter_set):
        self.letter_set = letter_set


    # processes the filter and displays the results
    def process(self):
        print('Playing Wordsearch! Have fun!')
        print()

        filter = ''
        self.letter_set = input('Letter set: ')
        if self.letter_set == '':
            return

        # get all words that contain these letters
        # includes words that are a subset of the letter set
        base_words = self.filter_set(self.words, self.letter_set)
        print(f'There are {len(base_words)} to choose from out of {len(self.words)} words')

        while True:
            filter = input("Filter: ").casefold()
            if filter == '':
                return

            filtered_words = super().filter_words(base_words, filter)
            print(f'Found {len(filtered_words)} words')

            super().print_words(filtered_words)


    def filter_set_handler(self, words):
        results = []
        set = self.set

        for word in words:
            if self.contains_set(word, set):
                results.append(word)
        
        return results


    def filter_set_parallel(self, words, set):
        self.set = set
        results = []
        count = int(len(words) / self.pool_size)

        print(f'Beginning parallel processing loop with pool size of {self.pool_size} and estimated chunk size of {count}')

        with Pool(self.pool_size) as pool:
            for result in pool.imap_unordered(self.filter_set_handler, words, count):
                results.append(result)
            pool.close()

        print(f'Total matches: {len(results)}')
        return results


    # filters a list of words based on all possible letters
    def filter_set(self, words, set):
        results = []
        for word in words:
            if self.contains_set(word, set):
                results.append(word)

        return results


    # returns the word if it contains all the letters in the set
    def contains_set(self, word, set):
        matches = 0
        for l in word:
            if set.find(l) > -1:
                matches += 1
                set = set.replace(l, '', 1)
                if len(set) == 0:
                    break
        
        if matches == len(word):
            return word
