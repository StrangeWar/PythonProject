import pandas

error = True


nato_alphabets = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_alphabets_dict = {row.letter: row.code for (index, row) in nato_alphabets.iterrows()}


def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        nato_phonetic_name = [nato_alphabets_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        generate_phonetic()
    else:
        print(nato_phonetic_name)


generate_phonetic()


