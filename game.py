import random;

def main():
    print(generateCode());

def generateCode():
    # genrerate 4 numbers and put them into an array

    firstNumber = random.randint(0,9)
    secondNumber = random.randint(0,9)
    thirdNumber = random.randint(0,9)
    fourthNumber = random.randint(0,9)

    codeArray = [firstNumber,secondNumber,thirdNumber,fourthNumber]
    return codeArray;

main();