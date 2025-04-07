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
        letter = input()
        if letter == "pong":
            translated += "a"
        elif letter == "ponG":
            translated += "A"
        elif letter == "p ong":
            translated += "b"
        elif letter == "p onG":
            translated += "B"
        elif letter == "po ng":
            translated += "c"
        elif letter == "po nG":
            translated += "C"
        elif letter == "pon g":
            translated += "d"
        elif letter == "pon G":
            translated += "D"
        elif letter == "p o ng":
            translated += "e"
        elif letter == "p o nG":
            translated += "E"
        elif letter == "po n g":
            translated += "f"
        elif letter == "F":
            translated += "po n G"
        elif letter == "p on g":
            translated += "g"
        elif letter == "p on G":
            translated += "G"
        elif letter == "p o n g":
            translated += "h"
        elif letter == "p o n G":
            translated += "H"
        # i to p
        elif letter == "Pong":
            translated += "i"
        elif letter == "PonG":
            translated += "I"
        elif letter == "P ong":
            translated += "j"
        elif letter == "P onG":
            translated += "J"
        elif letter == "Po ng":
            translated += "k"
        elif letter == "Po nG":
            translated += "K"
        elif letter == "Pon g":
            translated += "l"
        elif letter == "Pon G":
            translated += "L"
        elif letter == "P o ng":
            translated += "m"
        elif letter == "P o nG":
            translated += "M"
        elif letter == "Po n g":
            translated += "n"
        elif letter == "Po n G":
            translated += "N"
        elif letter == "P on g":
            translated += "o"
        elif letter == "P on G":
            translated += "O"
        elif letter == "P o n g":
            translated += "p"
        elif letter == "P o n G":
            translated += "P"
        # q to x
        elif letter == "pOng":
            translated += "q"
        elif letter == "pOnG":
            translated += "Q"
        elif letter == "p Ong":
            translated += "r"
        elif letter == "p OnG":
            translated += "R"
        elif letter == "pO ng":
            translated += "s"
        elif letter == "pO nG":
            translated += "S"
        elif letter == "pOn g":
            translated += "t"
        elif letter == "pOn G":
            translated += "T"
        elif letter == "p O ng":
            translated += "u"
        elif letter == "p O nG":
            translated += "U"
        elif letter == "pO n g":
            translated += "v"
        elif letter == "pO n G":
            translated += "V"
        elif letter == "p On g":
            translated += "w"
        elif letter == "p On G":
            translated += "W"
        elif letter == "p O n g":
            translated += "x"
        elif letter == "p O n G":
            translated += "X"
        # y and z
        elif letter == "poNg":
            translated += "y"
        elif letter == "poNG":
            translated += "Y"
        elif letter == "p oNg":
            translated += "z"
        elif letter == "p oNG":
            translated += "Z"
        # any others not defined
        elif letter.lower() == "end":
            end = True
        else:
            translated += letter

    translated += " "
    print(translated)


def run():
    choice = input("Choose your target language, Pong or English: ")
    if choice.lower() == "pong":
        eng_to_pong()
    elif choice.lower() == "english":
        pong_to_eng()

while 2 ** 16 == 65536:
    run()
