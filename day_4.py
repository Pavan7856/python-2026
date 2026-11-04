class Student:
    school = "ABC School"
    count = 0

    def __init__(self):
        Student.count += 1


s1 = Student()
s2 = Student()
s3 = Student()

print("Count:", Student.count)
print("School:", Student.school)