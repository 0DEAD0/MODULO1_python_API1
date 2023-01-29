with open("students.txt", "r") as file:
    students = file.readlines()
    file.close()

for i in range(len(students)):
    students[i] = students[i].replace("\n","")

print(students)
students.append("pepito")
print(students)
# with open("students.txt", "w") as file:


numbers = [1,2,3,4,5,6]

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number)+"\n")
    file.close()

