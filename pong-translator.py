def eng_to_pong():
    translated = ""
    print("ENTER TEXT BELOW: ")
    message = input()
    translated += "("
    for letter in message:
        if letter == "a":
            translated += "pong"
        elif letter == "A":
            translated += "ponG"
        elif letter == "b":
            translated += "p ong"
        elif letter == "B":
            translated += "p onG"
        elif letter == "c":
            translated += "po ng"
        elif letter == "C":
            translated += "po nG"
        elif letter == "d":
            translated += "pon g"
        elif letter == "D":
            translated += "pon G"
        elif letter == "e":
            translated += "p o ng"
        elif letter == "E":
            translated += "p o nG"
        elif letter == "f":
            translated += "po n g"
        elif letter == "F":
            translated += "po n G"
        elif letter == "g":
            translated += "p on g"
        elif letter == "G":
            translated += "p on G"
        elif letter == "h":
            translated += "p o n g"
        elif letter == "H":
            translated += "p o n G"
        # i to p
        elif letter == "i":
            translated += "Pong"
        elif letter == "I":
            translated += "PonG"
        elif letter == "j":
            translated += "P ong"
        elif letter == "J":
            translated += "P onG"
        elif letter == "k":
            translated += "Po ng"
        elif letter == "K":
            translated += "Po nG"
        elif letter == "l":
            translated += "Pon g"
        elif letter == "L":
            translated += "Pon G"
        elif letter == "m":
            translated += "P o ng"
        elif letter == "M":
            translated += "P o nG"
        elif letter == "n":
            translated += "Po n g"
        elif letter == "N":
            translated += "Po n G"
        elif letter == "o":
            translated += "P on g"
        elif letter == "O":
            translated += "P on G"
        elif letter == "p":
            translated += "P o n g"
        elif letter == "P":
            translated += "P o n G"
        # q to x
        elif letter == "q":
            translated += "pOng"
        elif letter == "Q":
            translated += "pOnG"
        elif letter == "r":
            translated += "p Ong"
        elif letter == "R":
            translated += "p OnG"
        elif letter == "s":
            translated += "pO ng"
        elif letter == "S":
            translated += "pO nG"
        elif letter == "t":
            translated += "pOn g"
        elif letter == "T":
            translated += "pOn G"
        elif letter == "u":
            translated += "p O ng"
        elif letter == "U":
            translated += "p O nG"
        elif letter == "v":
            translated += "pO n g"
        elif letter == "V":
            translated += "pO n G"
        elif letter == "w":
            translated += "p On g"
        elif letter == "W":
            translated += "p On G"
        elif letter == "x":
            translated += "p O n g"
        elif letter == "X":
            translated += "p O n G"
        # y and z
        elif letter == "y":
            translated += "poNg"
        elif letter == "Y":
            translated += "poNG"
        elif letter == "z":
            translated += "p oNg"
        elif letter == "Z":
            translated += "p oNG"
        # any others not defined + word seperation
        elif letter == " ":
            translated += ")("
        else:
            translated += letter
        translated += " "
    translated += ")"
    print(translated)

# Credit to AJH for this subroutine and the next one
def pong_to_eng_dict():
    return {
        "pong": "a",
        "p ong": "b",
        "po ng": "c",
        "pon g": "d",
        "p o ng": "e",
        "po n g": "f",
        "p on g": "g",
        "p o n g": "h",
        "Pong": "i",
        "P ong": "k",
        "Po ng": "j",
        "Pon g": "l",
        "P o ng": "m",
        "Po n g": "n",
        "P on g": "o",
        "P o n g": "p",
        "pOng": "q",
        "p Ong": "r",
        "pO ng": "s",
        "pOn g": "t",
        "p O ng": "u",
        "pO n g": "v",
        "p On g": "w",
        "p O n g": "x",
        "poNg": "y",
        "p oNg": "z",
    }

# Credit to AJH for this 
def fast_eng_to_pong(message):
    """A fast but less accurate pong-to-english translator. Unreliable for all dialects of pong."""
    valid_characters = ["p", "o", "n", " ", "P", "O", "N"]                # g is not in here. this will make sense later
    pong_dict = pong_to_eng_dict()                      # dictionary for pong>eng translations
    translation = ""
    current_pong = ""
    for character in message:                                      # for each character in the string

        # to prevent pong separation in the message from throwing the program off
        if current_pong == "" and character == " ":
            pass

        elif character in valid_characters:
            current_pong += character

        # each pong starts with p and ends with g, no matter what.
        # so by testing where the g is, we can find where each character ends and the next one starts.
        elif character == "g":
            current_pong += character
            translation += pong_dict[current_pong]
            current_pong = ""
        # in case it is uppercase
        elif character == "G":
            current_pong += "g"
            translation += pong_dict[current_pong].upper()
            current_pong = ""

        elif character == ")":                                 # ) identify when the word ends.
            translation += " "

        # this is to take care of special characters like commas or exclamation points.
        elif character != "(":               # ( are not necessary when we know ) end a word
            translation += character

        print(translation)


def run():
    choice = input("Choose your target language, Pong or English: ")
    if choice.lower() == "pong":
        eng_to_pong()
    elif choice.lower() in ["english", "eng"]:
        pong_to_eng()

while True:
    run()
