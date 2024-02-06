#Day5-Task1#
print("Day5-Task1")
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")



#Day5-Task2#
print("Day5-Task2")
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
        
        
        
#Day5-Task3#
print("Day5-Task3")
target = int(input())
even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)            


#Day5-Task4#
print("Day5-Task4")
target = 100
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)