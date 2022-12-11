Word Search
===========

Python program that uses a dictionary to help find words based on length, starting, ending, and contains characters.

## Create a virtual python env

[venv](https://docs.python.org/3/library/venv.html)

`python3 -m venv /path/to/new/virtual/environment`

## Download word file
[word list](https://github.com/kirasglimmer/wordsearch/raw/main/words.zip)


## Usage

usage:
    wordsearch.py <filter> <letter set> (<Y/y>)
    filter:
        specific letter (a-z) or any letter (#)
    letter set:
        only use words that contain all the letters in the set    
    Y/y:
        exclusive search, means don't reuse letters in letter set
        (not supported)

