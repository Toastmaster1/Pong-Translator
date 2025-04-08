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


def pong_to_eng():
    end = False
    translated = ""
    print("Enter each pong individually, starting at P and ending at G.")
    print("If there is a )( please enter a space.")
    print("Enter 'end' to finish translating.")
    while end is not True:
        print("ENTER THE NEXT PONG: ")
        pong = input()
        if pong == "pong":
            translated += "a"
        elif pong == "ponG":
            translated += "A"
        elif pong == "p ong":
            translated += "b"
        elif pong == "p onG":
            translated += "B"
        elif pong == "po ng":
            translated += "c"
        elif pong == "po nG":
            translated += "C"
        elif pong == "pon g":
            translated += "d"
        elif pong == "pon G":
            translated += "D"
        elif pong == "p o ng":
            translated += "e"
        elif pong == "p o nG":
            translated += "E"
        elif pong == "po n g":
            translated += "f"
        elif pong == "F":
            translated += "po n G"
        elif pong == "p on g":
            translated += "g"
        elif pong == "p on G":
            translated += "G"
        elif pong == "p o n g":
            translated += "h"
        elif pong == "p o n G":
            translated += "H"
        # i to p
        elif pong == "Pong":
            translated += "i"
        elif pong == "PonG":
            translated += "I"
        elif pong == "P ong":
            translated += "j"
        elif pong == "P onG":
            translated += "J"
        elif pong == "Po ng":
            translated += "k"
        elif pong == "Po nG":
            translated += "K"
        elif pong == "Pon g":
            translated += "l"
        elif pong == "Pon G":
            translated += "L"
        elif pong == "P o ng":
            translated += "m"
        elif pong == "P o nG":
            translated += "M"
        elif pong == "Po n g":
            translated += "n"
        elif pong == "Po n G":
            translated += "N"
        elif pong == "P on g":
            translated += "o"
        elif pong == "P on G":
            translated += "O"
        elif pong == "P o n g":
            translated += "p"
        elif pong == "P o n G":
            translated += "P"
        # q to x
        elif pong == "pOng":
            translated += "q"
        elif pong == "pOnG":
            translated += "Q"
        elif pong == "p Ong":
            translated += "r"
        elif pong == "p OnG":
            translated += "R"
        elif pong == "pO ng":
            translated += "s"
        elif pong == "pO nG":
            translated += "S"
        elif pong == "pOn g":
            translated += "t"
        elif pong == "pOn G":
            translated += "T"
        elif pong == "p O ng":
            translated += "u"
        elif pong == "p O nG":
            translated += "U"
        elif pong == "pO n g":
            translated += "v"
        elif pong == "pO n G":
            translated += "V"
        elif pong == "p On g":
            translated += "w"
        elif pong == "p On G":
            translated += "W"
        elif pong == "p O n g":
            translated += "x"
        elif pong == "p O n G":
            translated += "X"
        # y and z
        elif pong == "poNg":
            translated += "y"
        elif pong == "poNG":
            translated += "Y"
        elif pong == "p oNg":
            translated += "z"
        elif pong == "p oNG":
            translated += "Z"
        # any others not defined
        elif pong.lower() == "end":
            end = True
        else:
            translated += pong

    translated += " "
    print(translated)


def run():
    choice = input("Choose your target language, Pong or English: ")
    if choice.lower() == "pong":
        eng_to_pong()
    elif choice.lower() in ["english", "eng"]:
        pong_to_eng()

while True:
    run()
