import re


def IsValidNumber(cardNumber):
    return cardNumber.isdigit() and len(cardNumber) in [13, 15, 16]


def getCheckSum(cardNumber):
    checkSum = 0
    for i, char in enumerate(reversed(cardNumber)):
        digit = int(char)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checkSum += digit
    return checkSum


def isValidCheckSum(checkSum):
    return checkSum % 10 == 0


def getCardType(string):
    if len(string) == 13 or len(string) == 16 and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and string.startswith("34") or string.startswith("37"):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid"


cardNumber = input("Enter Card Number: ")
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        print(getCardType(cardNumber))
    else:
        print('Not Valid')
        print(getCardType(cardNumber))
else:
    print("Wrong Input. Try again...")