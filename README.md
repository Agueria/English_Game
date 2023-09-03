# Flashy - Flashcard App

## Introduction

Flashy is a simple flashcard app built with Python and Tkinter. The application aims to help users learn French words by showing flashcards that flip to reveal the English translation. It also includes features to keep track of words that the user is yet to learn.

## Features

- Easy-to-use graphical user interface built with Tkinter
- Flashcards display French words, and flip after 3 seconds to show the English translation
- The application keeps track of words you have yet to learn
- All data is stored locally, so your learning progress is saved

## Dependencies

- Python 3.x
- Tkinter
- Pandas

## How to Use

1. Clone this repository
    ```shell
    git clone https://github.com/your-username/Flashy.git
    ```
2. Install Pandas if you haven't
    ```shell
    pip install pandas
    ```
3. Run the `main.py` script
    ```shell
    python main.py
    ```
4. The application window should open. Click the "Right" button if you know the word, and the "Wrong" button if you don't. The flashcards will update accordingly.

## Project Structure

- `main.py`: The main script that runs the application.
- `data/french_words.csv`: Contains the original list of French words and their English translations.
- `data/words_to_learn.csv`: Contains the list of words that the user has yet to learn. (This file is created automatically.)

## Contributing

Feel free to contribute to this project by submitting pull requests or issues.

## License

This project is open-source and available under the [MIT License](LICENSE).
