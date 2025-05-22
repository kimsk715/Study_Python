student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

print(student["name"])
print(student.get("email"))
print(student.get("phone", "01012341234"))

if 'name' in student:
    student['email'] = 'test@gmail.com'

print(student)

del student['email']

print(student)

my_dict = {
    1: "한동석",
    False: [10, 20, 30]
}

print(my_dict[10 < 11])

print(list(student.keys()))

for i in student.keys():
    print(i)

print(list(student.values()))

for key, value in student.items():
    print(key, value)