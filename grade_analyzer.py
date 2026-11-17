print("Student Grade Analyzer")

student = "Alex"
grade = 82

print("Student:", student)
print("Grade:", grade)

if grade >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

if grade >= 90:
    category = "A"
elif grade >= 80:
    category = "B"
elif grade >= 70:
    category = "C"
elif grade >= 60:
    category = "D"
else:
    category = "F"

print("Category:", category)

