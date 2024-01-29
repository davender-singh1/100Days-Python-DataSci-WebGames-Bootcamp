#Day2-Task1
print("Day2-Task1")
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)


#Day2-Task2
print("Day2-Task2")
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weight = int(weight)
height = float(height)
BMI = weight / (height * 2)
BMI_as_int = int(BMI)
print(BMI_as_int)

#Day2-Task3
print("Day2-Task3")
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} left.")


