import sys, getopt


# loads the word database in an array, converts each word to lowercase
# returns the array of words
def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    results = []
    for word in valid_words:
        results.append(word.casefold())

    return results


# matches a word to the filter
def match_word(word, filter):
    if len(word) != len(filter):
        print(f'Error: word {word} is different length than filter {filter}')
        exit()

    match = False
    for i in range(len(word)):
        if filter[i] == '#':
            continue
        if word[i] != filter[i]:
            return

    return word


# returns the word if it contains all the letters in the set
def contains_set(word, set, exclusive):
    matches = 0
    for w in word:
        if set.find(w) < 0:
            break

        matches += 1
        if exclusive == False:
            continue

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
def filter_words(words, filter):
    results = []
    length = len(filter)
    for word in words:
        if len(word) != length:
            continue
        
        if match_word(word, filter):
            results.append(word)

    return results


# filters a list of words based on all possible letters
def filter_set(words, set, exclusive):
    results = []
    for word in words:
        if contains_set(word, set, exclusive):
            results.append(word)

    return results


# gets all the words of the specified length
def get_words(words, filter):
    results = []
    length = len(filter)
    for word in words:
        if len(word) != length:
            continue
        
        if match_word(word, filter):
            results.append(word)
    
    return results


# displays the help
def show_help():
    print('finds matching words using a filter and a set of letters')
    print('usage: wordsearch.py <filter> <letter set>')
    print()
    exit()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Missing required parameters')
        show_help()
    
    filter = sys.argv[1]
    letter_set = sys.argv[2]
    exclusive = False
    if len(sys.argv) > 3:
        exclusive = (sys.argv[3].casefold() == 'y')

    # get all the words
    all_words = load_words()

    # filter the wordlist
    filtered_words = get_words(all_words, filter)

    # get all the words containing the letter set
    words_in_set = filter_set(filtered_words, letter_set, exclusive)

    print(f'All the words matching {filter} with the letter set {letter_set} using an exclusive filter {exclusive}:')
    print()
    if len(words_in_set) > 0:
        for word in words_in_set:
            print(f'{word}')
    else:
        print('No words found')

    print()

