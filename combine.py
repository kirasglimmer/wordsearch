

# loads the word database in an array, converts each word to lowercase
# returns the array of words
def load_words(file_name):
    with open(file_name) as word_file:
        raw = word_file.read().split()
        word_set = set(raw)

    results = set()
    for word in word_set:
        results.add(word.casefold())

    return results


def combine_lists(lista, listb):
    return lista.union(listb)


def write_list(list, file_name):
    with open(file_name, 'w') as word_file:
        for word in list:
            word_file.write(f'{word}\n')


if __name__ == '__main__':
    words = load_words('words.txt')
    words2 = load_words('words2.txt')

    all_words = words2.union(words2)
    if len(all_words) != len(words2):
        print(f'Added {len(words) - len(words2)} words to the list')
        write_list(all_words, 'newlist.txt')
    else:
        print('No changes to the word list')

