import random
import pyperclip

def word_randomizer(sentence):
    words = sentence.split(' ')
    new_sentence = list()
    for i in range(len(words)):
        chosen = random.choice(words)
        new_sentence.append(chosen)
        words.remove(chosen)
    return ' '.join(new_sentence)

def main():
    while True:
        text = input('Sentence to be randomized: ')
        if not text:
            break
        word = word_randomizer(text)
        pyperclip.copy(word)
        print(word + '\n')

if __name__ == '__main__':
    main()