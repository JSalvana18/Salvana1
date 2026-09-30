# Practice 3
students={}
number = int(input("Enter a number: "))
for i in range (number):
    print("\nStudent, i + 1")
    name = input("Enter student name: ")
    grade1 = float(input("Enter grade of first student: "))
    grade2 = float(input("Enter grade of second student: "))
    grade3 = float(input("Enter grade of third student: "))
    students[name] = (grade1 , grade2 ,grade3)
print("\n===== STUDENT RECORDS ======")
highest = 0
namehghest = ""
tally = 0
for name, grades in students.items():
    average = sum(grades)/len(grades)
    print(name,*grades,"Average", round(average, 2))
    #find highes > highest:
    highest = average
    namehighest = name