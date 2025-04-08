dna_trans = {'a':'t',
             't':'a',
             'c':'g',
             'g':'c',
             'u':'a'
             }

def translate(st):
    new = []
    for i, let in enumerate(st.lower().replace(' ', '')):
        if let in dna_trans:
            new.append(dna_trans[let])
            if i+1 % 3 == 0:
                new.append(' ')
    return ''.join(new).upper()

def main():
    while True:
        setting = input('DNA or RNA? ').lower()
        if not setting:
            break
        if not setting in ['dna', 'rna']:
            continue
        seq = input("Enter nucleotide sequence to be translated its complimentary sequence: ").lower()
        out = translate(seq)
        if setting == 'dna':
            print(out, '\n')
        elif setting == 'rna':
            print(out.replace('T','U'), '\n')

if __name__ == '__main__':
    main()