# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_student_heights = 0
num_students = 0

for height in student_heights:
  sum_student_heights += height
  num_students += 1

result = sum_student_heights / num_students

print(f"The Avarage Height is {round(result)}")
