#!/bin/sh


if [ ! -f words.txt ]; then
    if [ -f words.zip ]; then
        echo "Extracting words.txt dictionary file"
        unzip words.zip
    else
        echo "Unable to extract words.txt - please download a words.zip dictionary"
    fi
fi

if [ ! -f pyvenv.cfg ]; then
    echo "Establishing python virtual environment"
    python3 -m venv "$PWD"
fi

echo "Setup complete"
