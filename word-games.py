import sys, getopt
from src.word_loader import WordLoader
from src.wordsearch import WordSearch



# returns a typle with the type of the game
def get_game():
    word_loader = WordLoader('words.txt')
    all_words = word_loader.get_words()

    print("Choose game type:")
    print("  Wordsearch [s]")
    print("  Wordle [l]")
    game_type = input("Type:")
    match game_type:
        case "s":
            return WordSearch(all_words)
        case "l":
            return "abcdefghijklmnopqrstuvwyxz", False

    print(f'Unknown game type: "{game_type}"')
    return get_game()


# displays the help
def show_help():
    print('finds matching words using a filter and a set of letters')
    print('usage: python word-games.py')
    print()
    exit()


# 
if __name__ == '__main__':
    # get all the words
    word_loader = WordLoader('words.txt')
    all_words = word_loader.get_words()

    game = get_game()

    game.process()
