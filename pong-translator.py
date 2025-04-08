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

def eng_to_pong_dict():
    return {
        "a": "pong",
        "b": "p ong",
        "c": "po ng",
        "d": "pon g",
        "e": "p o ng",
        "f": "po n g",
        "g": "p on g",
        "h": "p o n g",
        "i": "Pong",
        "k": "P ong",
        "j": "Po ng",
        "l": "Pon g",
        "m": "P o ng",
        "n": "Po n g",
        "o": "P on g",
        "p": "P o n g",
        "q": "pOng",
        "r": "p Ong",
        "s": "pO ng",
        "t": "pOn g",
        "u": "p O ng",
        "v": "pO n g",
        "w": "p On g",
        "x": "p O n g",
        "y": "poNg",
        "z": "p oNg",
    }


def eng_to_pong():
    message = input("Please enter your text in English: ")
    eng_dict = eng_to_pong_dict()
    translation = "("
    for letter in message:
        if letter == " ":
            translation += ")("
        else:
            try:
                translation += eng_dict[letter]
            except KeyError:
                pong_translation = eng_dict[letter.lower()]
                pong_translation = pong_translation[:-1] + pong_translation[-1].upper()
                translation += pong_translation
            translation += " "
    translation += ")"
    print(translation)

# Credit to AJH for this
def pong_to_eng():
    message = input("Please enter your message in Pong: ")
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
