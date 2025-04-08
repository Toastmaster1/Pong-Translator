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

    return translation