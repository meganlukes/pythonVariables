word = input("Give me a word ")
print("The first letter in " + word + " is " + word[0] + ".")
number = input("Give me a number to double: ")
number = int(number)
newNumber = number * 2
print("Your new number is " + str(newNumber) + ".")
number = int(input("Give me a new number: "))
secondNumber = int(input("Give me a second number: "))
newNumber = number ** secondNumber
print(str(number) + " to the power of " + str(secondNumber) + " is " + str(newNumber) + ".")