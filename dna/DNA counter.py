def counter(txt, instance):
    return txt.count(instance), txt.split(instance)

def main():
    dna = input('Enter DNA: ')
    search = input('Enter instance to search for: ')
    num, listed_dna = counter(dna, search)
    print(num)
    print(listed_dna)

if __name__ == '__main__':
    main()