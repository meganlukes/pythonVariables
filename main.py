#manipulate strings
# word = input("Give me a word ")
# print("The first letter in " + word + " is " + word[0] + ".")

#math functions
# number = input("Give me a number to double: ")
# number = int(number)
# new_number = number * 2
# print("Your new number is " + str(new_number) + ".")
# number = int(input("Give me a new number: "))
# second_number = int(input("Give me a second number: "))
# new_number = number ** second_number
# print(str(number) + " to the power of " + str(second_number) + " is " + str(new_number) + ".")
# new_number = int(input("Give me a number to halve and round down: "))  // 2
# print(f"The new number is {new_number}")

#BMI calculator
# print("Let's calculate your BMI")
# kg_weight = float(input("How much do you weigh (in pounds)? ")) * 0.45359237
# m_height = float(input("How tall are you in inches? ")) * 2.54 / 100
# bmi = round(kg_weight / (m_height * m_height), 1)
# print("Your BMI is " + str(bmi) + ".")

#How many weeks you'll live
# weeks = int(int(input("For how many years do you think you'll live? ")) * 52.17857)
# print(f"You can expect to live about  {weeks} weeks.")

#Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give? "))
people = float(input("How many people are splitting the bill? "))
tip = tipPercent * bill / 100
bill += tip
perPersonBill = round(bill / people, 2)
print(f"Each person should pay ${perPersonBill}.")