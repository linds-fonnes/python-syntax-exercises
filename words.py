def print_upper_words(words,must_start_with):
    """
    prints each word in list as uppercase
    """
    for word in words:
        if any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())

print_upper_words(["hello","hey","egoodbye","yo","yes","burgundy","pink","purple"],must_start_with={"h","y"})