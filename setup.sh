#!/bin/sh


if [ ! -f words.txt ]; then
    if [ ! -f words.zip ]; then
        echo "Downloading dictionary zip file"
        curl -LO https://github.com/kirasglimmer/wordsearch/raw/main/words.zip
    fi

    echo "Extracting dictionary file"
    unzip words.zip
fi

if [ ! -f pyvenv.cfg ]; then
    echo "Establishing python virtual environment"
    python3 -m venv "$PWD"
fi

echo "Setup complete"
