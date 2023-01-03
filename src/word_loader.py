import sys


class WordLoader:
    """Loads the raw word list"""

    dictionary_path = ''
    word_list = None

    def __init__(self, path):
        self.dictionary_path = path
        self.word_list = self.load_words(self.dictionary_path)

    # loads the word database in an array, converts each word to lowercase
    # returns the array of words
    def load_words(self, file_name):
        with open(file_name) as word_file:
            valid_words = set(word_file.read().split())

        results = []
        for word in valid_words:
            results.append(word.casefold())

        #print(f'Loaded {len(results)} words')
        return set(results)


    def get_words(self):
        """Returns the list of words"""
        return self.word_list


