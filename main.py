
MAX_TRIES = 6

HANGMAN_ASCII_ART = f"""
 Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
 Maximum tries: {MAX_TRIES}
"""

HANGMAN_PHOTOS = {
    0: """
    x-------x
    """,
    1: """
    x-------x
    |
    |
    |
    |
    |
    """,
    2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |
    """
}


# Checks if the entered letter is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1:
        return False
    if letter_guessed in old_letters_guessed:
        return False
    if letter_guessed.isalpha():
        return True
    return False


# Adds the entered letter to guess list if its valid
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(' -> '.join(old_letters_guessed))
        return False


# Returns a representation of the current progression of the games guesses
def show_hidden_word(secret_word, old_letters_guessed):
    res = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            res += letter + " "
        else:
            res += "_ "
    return res


# Checks if the secret word has been completely guessed
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# Prints the hangman photo based on the num of failed guesses
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


# Chooses a word from the file based on user input
def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
    num_unique_words = len(set(words))
    word_index = (index - 1) % len(words)
    return num_unique_words, words[word_index]


# Handles the main progression of the game
def main():
    print(HANGMAN_ASCII_ART)
    file_path = input("Enter file path: ")
    index = int(input("Enter index of a word in the file: "))
    secret_word = choose_word(file_path, index)[1]
    old_letters_guessed = []
    num_of_tries = 0
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while not check_win(secret_word, old_letters_guessed) and num_of_tries <= MAX_TRIES:
        letter_guessed = input("Guess a letter: ").lower()
        result = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        while not result:
            letter_guessed = input("Enter a valid letter: ").lower()
            result = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if letter_guessed in secret_word:
            print("Correct Guess :)")
            print(show_hidden_word(secret_word, old_letters_guessed))

        else:
            print("Wrong Guess :(")
            num_of_tries += 1
            if num_of_tries <= MAX_TRIES:
                print_hangman(num_of_tries)
            print(show_hidden_word(secret_word, old_letters_guessed))

    if num_of_tries > MAX_TRIES:
        print(f"LOSE \nthe word was: {secret_word}")
    else:
        print("WIN")


if __name__ == "__main__":
    main()
