# Q36.

full_name = input("Enter full name: ")
name_parts = full_name.split()

print(name_parts[0])
print(name_parts[1])
print(name_parts[2])


# Q37.

first_name, last_name = input("Enter first and last name: ").split()

print("First Name:", first_name)
print("Last Name:", last_name)


# Q38.

a, b, c = input("Enter three numbers: ").split()
a = int(a)
b = int(b)
c = int(c)

print(a + b + c)


# Q39.

record = input("Enter student record: ")
name, age, course, city = record.split(",")

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)


# Q40.

email = input("Enter email address: ")
username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)


# Q41.

sentence = input("Enter a sentence: ")
words = sentence.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))