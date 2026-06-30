student = {
    "id": 1,
    "name": "vignesh",
    "department": "CSE"
}

print(student["name"])
print(student["department"])
student["name"] = "Deva"
print(student["name"])

student["marks"] = 480
print(student)

student.pop("marks")
print(student)

# student.clear()

for key in student:
    print(key)

for value in student.values():
    print(value)

for key ,value in student.items():
    print(key, ":", value)
