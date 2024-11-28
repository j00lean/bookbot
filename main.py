alphabet = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
        "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
        }

def count_characters(text):
    for character in text.lower():
        if character in alphabet:
            alphabet[character] += 1
    return alphabet

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main ():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    letter_count = count_characters(text)
    print(f"There are {num_words} words")
    for letter in alphabet:
        print(f"The letter {letter} was found {alphabet[letter]} times")

main()
