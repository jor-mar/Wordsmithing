from english_words import get_english_words_set
import pyperclip

words = get_english_words_set(['web2'], lower=True, alpha=True)

modes = {'red': -1,
         'green': 1,
         'largest': -1,
         'smallest': 1}

def tea(term, lead=-1):
    local_set = set()
    if not term.isalpha():
        return 'Not enough words fit that mode!'
    for word in words:
        if term in word:
            local_set.add(word)
    if len(local_set) <= abs(lead)+1:
        return 'Not enough words fit that mode!'
    return sorted(local_set, key=len)[lead]

def main():
    while True:
        mode = input('Enter a mode: ').lower()
        while mode in modes:
            word = input('Enter parameter: ').lower()
            if not word:
                print()
                break
            word = tea(word, modes[mode])
            pyperclip.copy(word)
            print(word)
        if not mode:
            break

if __name__ == '__main__':
    main()