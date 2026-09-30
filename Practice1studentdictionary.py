#Practice1
students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 70,
    "Diana": 95
}
print("STUDENT GRADES")
print("------------------")
print("Ana", students["Ana"])
print("Ben", students["Ben"])

# Add a new student
students["Ella"] =88
# Update a student grade
students["Carlo"]= 82
students["Diana"]= 91
name1 = input("Enter student name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("-------------------------")
for name,grade in students.items():
    print(name,'-',grade)
# Search for a student
search= input("\nEnter name to search for: ")
if search in students:
    print(search, "has a grade of ", students[search])
else:
    print("Student not found")
    highest=max(students, key=students.get)
    print(highest)