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
words_list = filter_words(length, remove_special_characters(open_word_file(file)))
random_word = choose_random_word(words_list)
random_list = list(random_word)
print(random_word)

recap_feedback = []  # List to store feedback for each guess

attempts = 6  # Number of attempts allowed
win = False

while attempts > 0 and not win:
    
    for feedback_line in recap_feedback:
        print(' '.join(feedback_line))

    guess = input(f"Enter a {length}-letter word: ").strip().lower()
    
    if len(guess) != length:
        print(f"Please enter a word with exactly {length} letters.")
        continue
    
    if guess not in words_list:
        print("This word is not in the list. Try again.")
        continue
    
    feedback = []
    for i, letter in enumerate(guess):
        if letter == random_list[i]:
            feedback.append(letter.upper())  # Correct letter in correct position
        elif letter in random_list:
            feedback.append(letter)  # Correct letter but wrong position
        else:
            feedback.append('.')  # Incorrect letter
    recap_feedback.append(feedback)
    
    #print("Feedback:", ' '.join(feedback))
    
    if guess == random_word:
        win = True
        print("Congratulations! You've guessed the word:", random_word)
    
    attempts -= 1


