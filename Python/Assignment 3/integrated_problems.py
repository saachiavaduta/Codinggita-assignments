# Q60.

name = input("Enter student name: ")
marks1, marks2, marks3 = input("Enter three subject marks: ").split()
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")


# Q61.

student_id = input("Enter student ID: ")
degree, batch, branch, roll_number = student_id.split("-")

print("Degree:", degree)
print("Batch:", batch)
print("Branch:", branch)
print("Roll Number:", roll_number)

last_three = student_id[-3:]
roll_number = int(roll_number)
print(roll_number)


# Q62.

full_name = input("Enter full name: ")
first_name, middle_name, last_name = full_name.split()

username = first_name.lower() + "." + last_name.lower()
print(username)


# Q63.

sentence = input("Enter a sentence: ")
words = sentence.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Number of words:", len(words))


# Q64.

email = input("Enter email address: ")
has_at = "@" in email
username, domain = email.split("@")

print("@ Present:", has_at)
print("Username:", username)
print("Domain:", domain)


# Q65.

char = input("Enter a character: ")
code = ord(char)
previous_char = chr(code - 1)
next_char = chr(code + 1)

print("Character:", char)
print("Code:", code)
print("Previous:", previous_char)
print("Next:", next_char)


# Q66.

product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


# Q67.

date = input("Enter date (DD-MM-YYYY): ")
day, month, year = date.split("-")

print("Day:", day)
print("Month:", month)
print("Year:", year)

year_from_slice = date[-4:]
print(year_from_slice)


# Q68.

sentence = input("Enter two words: ")
first_word, second_word = sentence.split()

print("First Word:", first_word)
print("Second Word:", second_word)
print("First Word Reversed:", first_word[::-1])
print("Second Word Reversed:", second_word[::-1])


# Q69.

student_code = input("Enter student code: ")
degree, batch, branch, roll = student_code.split("-")

code = f"{degree}/{branch}/{roll}"

print("Degree:", degree)
print("Batch:", batch)
print("Branch:", branch)
print("Roll:", roll)
print("Code:", code)


# Q70.

full_name = input("Enter full name: ")
first_name, middle_name, last_name = full_name.split()

first_upper_part = first_name[0:3].upper()
last_lower_part = last_name[1:4].lower()
reversed_full = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper_part}")
print(f"Last Name (Lower Part): {last_lower_part}")
print(f"Full Name Reversed: {reversed_full}")