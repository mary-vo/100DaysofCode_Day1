######## Notes from lecture
'''
fruits = ["Apple", "Peach", "Pear"]
# for {name for the singular item} in {list, here fruits}
# Everything indented after for loop colon will be looped, without indentation (outside for loop), instructions will be carried out after the for loop
for fruit in fruits: 
  print(fruit)
  print(fruit + " Pie")
print(fruits)
'''

######## Exercise - Average Height
# Instructions
'''
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# print(student_heights)

# Using a for loop to convert a list of string to integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
# 🚨 Don't change the code above 👆 
#Write your code below this row 👇
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
# print(total_height)

number_of_students = 0 
for student in student_heights:
  number_of_students += 1
# print(number_of_students)

average = round(total_height / number_of_students)
print(average)