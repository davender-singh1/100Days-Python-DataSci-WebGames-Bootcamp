#Day4-Task1#
print("Day4-Task1")
import random
random_side = random.randint(0,1)
if random_side == 0:
    print("Heads")
else:
    print("Tails")
    
#Day4-Task2#
print("Day4-Task2")
import random
names_string = "John, Jane, Bob, Alice"
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")


#Day4-Task3#
print("Day4-Task3")
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")


