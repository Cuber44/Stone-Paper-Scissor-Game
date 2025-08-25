import random

key = ["stone","paper","scissor"]

def userinput(key):
    useroption = input(f"Enter one of your option from {key}: ").lower()
    if useroption in key:
        return useroption
    else:
        userinput()

def computerinput(key):
    compoption = key[random.randint(0,len(key))]
    return compoption

def matcher(uo,co,key):
    if uo == co:
        result = "Draw"
    elif uo == key[0] and co == key[1]:
        result = "Computer Won"
    elif uo == key[1] and co == key[2]:
        result = "Computer Won"
    elif uo == key[2] and co == key[0]:
        result = "Computer Won"
    elif uo == key[1] and co == key[0]:
        result = "You Won"
    elif uo == key[2] and co == key[1]:
        result = "You Won"
    elif uo == key[0] and co == key[2]:
        result = "You Won"
    return result+f". Your selection {uo} and computer's selection {co}."

def main(key):
    print("Welcome to the game")
    userselection = userinput(key)
    result = matcher(userselection,computerinput(key),key)
    print(result)

if __name__ == "__main__":
    main(key)