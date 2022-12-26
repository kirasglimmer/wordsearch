import signal
from src.word_loader import WordLoader
from src.wordsearch import WordSearch
from src.wordle import Wordle


def abort_handler(sig, frame):
    msg = 'Ctrl-c was pressed. Do you really want to exit? y/n '
    
    if input(msg).casefold() == 'y':
        print('')
        exit(1)


#signal.signal(signal.SIGINT, abort_handler)


# returns a typle with the type of the game
def get_game():
    word_loader = WordLoader('words.txt')
    all_words = word_loader.get_words()
    #print(f'Loaded {len(all_words)} words')

    print("Choose game type (empty to exit):")
    print("  Wordsearch: [s]")
    print("      Wordle: [l]")
    print("        Quit: [q]")
    game_type = input("Type: ").casefold()

    match game_type:
        case "s":
            return WordSearch(all_words)
        case "l":
            return Wordle(all_words)
        case '' | 'q':
            print('Exiting')
            exit()
        case other:
            print(f'Unknown game type: "{game_type}"')
            return get_game()


# displays the help
def show_help():
    print('finds matching words using a filter and a set of letters')
    print('usage: python word-games.py')
    print()
    exit()



if __name__ == '__main__':
    while True:
        try:
            get_game().process()
        except KeyboardInterrupt:
            print('Exiting')
            exit()
