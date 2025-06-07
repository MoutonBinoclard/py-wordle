# WORDLE GAME !

def open_word_file(file_name):
    with open(file_name, encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return words

def remove_special_characters(words):
    """
    Remove caracters like é, è, ê, ç, à, etc...
    """
    special_characters = "àâäçéèêëîïôœùûüÿ"
    remplacement_caras = "aaaceeeeiioouuuy"

    translation_table = str.maketrans(special_characters, remplacement_caras)
    return [word.translate(translation_table) for word in words]

def filter_words(length, words):
    """
    Filter words by length.
    """
    return [word for word in words if len(word) == length]

def choose_random_word(words):
    """
    Choose a random word from the list.
    """
    import random
    return random.choice(words)


length = 5  # Length of words to filter
file = "fr.txt"  # File containing the words

print("Loading words...")
words_list = filter_words(length, remove_special_characters(open_word_file(file)))
print (f"Loaded {len(words_list)} words of length {length}.")

random_word = choose_random_word(words_list)

win = False
attempts = 6  # Number of attempts allowed
print(f"Guess the {length}-letter word! You have {attempts} attempts.")

while attempts > 0 and not win:
    guess = input(f"Enter your {length}-letter guess: ").strip().lower()
    
    if len(guess) != length:
        print(f"Please enter a {length}-letter word.")
        continue
    
    if guess not in words_list:
        print("This word is not in the list. Try again.")
        continue
    
    if guess == random_word:
        win = True
        print("Congratulations! You've guessed the word!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")


