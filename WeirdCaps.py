import random
import pyperclip

def randomize_caps(word):
    new_word = list()
    for letter in list(word.lower()):
        if random.randint(0,1):
            new_word.append(letter.upper())
        else:
            new_word.append(letter)
    return ''.join(new_word)

def main():
    while True:
        text = input('Text to be randomly capitalized: ')
        if not text:
            break
        text_prime = randomize_caps(text)
        pyperclip.copy(text_prime)
        print(text_prime + '\n')

if __name__ == '__main__':
    main()