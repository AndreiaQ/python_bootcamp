with open("Input/Letters/starting_letter.txt", "r") as f:
    content_letter = f.read()

with open("Input/Names/invited_names.txt") as names:
    for line in names:
        name = line.strip()
        personalized_letter = content_letter.replace('[name]', name)
        with open(f"Output/ReadyToSend/letter_{name}.txt", "w") as letters_redy:
            letters_redy.write(personalized_letter)
