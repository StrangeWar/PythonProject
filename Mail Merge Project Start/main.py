PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./input/Letters/starting_letter.txt") as letter:
    content = letter.read()

for name in names:
    clean_name = name.strip()
    with open(f"./output/ReadyToSend/letter_for_{clean_name}.txt", 'w') as letter:
        new_content = content.replace(PLACEHOLDER, clean_name)
        letter.write(new_content)
