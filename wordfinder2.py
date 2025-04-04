import pyperclip

modes = {'red': -1,
         'green': 1,
         'largest': -1,
         'smallest': 1}

exclusions = {'-', "'"}


words = set()
with open('words.txt') as file:
    for line in file:
        excluded = False
        for exclusion in exclusions:
            if exclusion in line:
                excluded = True
                break
        if not excluded:
            words.add(line.strip())

def tea(term, lead=-1):
    local_set = set()
    for word in words:
        if term in word:
            local_set.add(word)
    if len(local_set) <= abs(lead)+1:
        return 'Not enough words fit that mode!'
    return sorted(local_set, key=len)[lead]

def main():
    while True:
        mode = input('Enter a mode: ').lower().strip()
        while mode in modes:
            parameter = input('Enter parameter: ').lower().strip()
            if not parameter:
                print()
                break
            word = tea(parameter, modes[mode])
            pyperclip.copy(word)
            print(word)
        if not mode:
            break

if __name__ == '__main__':
    main()