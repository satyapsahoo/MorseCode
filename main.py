# 1. The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.

morse_dict = {
    "A": ". _",
    "B": "_ . . .",
    "C": "_ . _ .",
    "D": "_ . .",
    "E": ".",
    "F": ". . _ .",
    "G": "_ _ .",
    "H": ". . . .",
    "I": ". .",
    "J": ". _ _ _",
    "K": "_ . _",
    "L": ". _ . .",
    "M": "_ _",
    "N": "_ .",
    "O": "_ _ _",
    "P": ". _ _ .",
    "Q": "_ _ . _",
    "R": ". _ .",
    "S": ". . .",
    "T": "_",
    "U": ". . _",
    "V": ". . . _",
    "W": ". _ _",
    "X": "_ . . _",
    "Y": "	_ . _ _",
    "Z": "_ _ . .",
    ".": ". _ . _ . _",
    ",": "_ _ . . _ _",
    " ": "       "
}

# Take user input and convert to upper case
user_input = input("Enter a statement to convert to morse code (Use alphabets, comma, full-stop only): ").upper()
word_list = user_input.split()  # Split the sentence to words
morse_list = []
for word in word_list:
    letter_list = list(word)  # Split individual word into letters
    for letter in letter_list:
        try:
            morse_code = morse_dict[letter]  # Find morse code for letter from dictionary
        except KeyError:
            morse_code = morse_dict[","]  # Convert non dictionary words to comma
        morse_list.append(morse_code)
        morse_list.append("   ")  # Add 3 spaces between letters
    morse_list.append(morse_dict[" "])  # Add 7 spaces between words
# Print morse code
morse_statement = str()
for code in morse_list:
    morse_statement = morse_statement + code
print(f"The morse code for {user_input} is:\n", morse_statement)
