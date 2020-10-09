import re

goAgain = 1
while goAgain == 1:


        validity = True
        while validity == True:
                try:
                        firstNumber = long(raw_input("Type the first number: "))
                        validity = False # If the user's input is good, exit the while loop
                except ValueError:
                        print("That's not a valid number, please re-enter the value ")
                        


        validity = True
        while validity == True:
                try:
                        secondNumber = long(raw_input("Type the second number: "))
                        validity = False # If the user's input is good, exit the while loop
                except ValueError:
                        print("That's not a valid number, please re-enter the value ")
                        


        mathChoice = str(raw_input("Enter Choice (+,-,*,/)"))

        if "+" in mathChoice.lower():
                print firstNumber, "+", secondNumber, "=", firstNumber + secondNumber
        elif "-" in mathChoice.lower():
                print firstNumber, "-", secondNumber, "=", firstNumber - secondNumber
        elif "*" in mathChoice.lower():
                print firstNumber, "*", secondNumber, "=", firstNumber * secondNumber
        elif "/" in mathChoice.lower():
                print firstNumber, "/", secondNumber, "=", firstNumber / secondNumber

        goAgain = int(raw_input("Type 1 to enter more numbers, or any other number to quit: "))

print "Goodbye!\n"
