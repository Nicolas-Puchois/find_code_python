import random;
import re;

def main():
    print(generateCode())
    print(playerInput());

def generateCode():
    # genrerate 4 numbers and put them into an array

    firstNumber = random.randint(0,9)
    secondNumber = random.randint(0,9)
    thirdNumber = random.randint(0,9)
    fourthNumber = random.randint(0,9)

    codeArray = [firstNumber,secondNumber,thirdNumber,fourthNumber]
    return codeArray;

def playerInput():
    #player input
    
    playerInput= input("entrer les chiffres de 0 à 9: ")

    isInputValid = isPlayerInputValid(playerInput)

    print(isInputValid)

    if(isInputValid):
        return playerInput;

    return playerInput;

def isPlayerInputValid(playerInput):
    return bool(re.fullmatch(r"[0-9]{1}", playerInput));

main();