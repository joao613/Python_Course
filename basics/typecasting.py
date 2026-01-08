name = "João"
no_name = ""
age = 25
grade = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(grade))
print(type(is_student))

grade = int(grade)
print(grade)

age = float(age)
print(age)
age += 1
print(age)

age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

name = bool(name)
print(name)

no_name = bool(no_name)
print(no_name)