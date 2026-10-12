# Q45.
text = input("Enter a string: ")
middle_index = len(text) // 2
print(text[middle_index])


# Q46.
text = input("Enter a string: ")
half = len(text) // 2
first_half = ""
second_half = ""
for i in range(len(text)):
    if i < half:
        first_half = first_half + text[i]
    else:
        second_half = second_half + text[i]
print("First Half:", first_half)
print("Second Half:", second_half)


# Q47.
text = input("Enter a string: ")
length = len(text)
half = length // 2
first_half = ""
middle = ""
second_half = ""
for i in range(length):
    if i < half:
        first_half = first_half + text[i]
    elif length % 2 == 1 and i == half:
        middle = middle + text[i]
    else:
        second_half = second_half + text[i]
print("First Half:", first_half)
if length % 2 == 1:
    print("Middle:", middle)
print("Second Half:", second_half)


# Q48.
text = input("Enter an even-length string: ")
half = len(text) // 2
is_equal = True
for i in range(half):
    if text[i] != text[half + i]:
        is_equal = False
if is_equal:
    print("Equal Halves")
else:
    print("Different Halves")


# Q49.
text = input("Enter a string: ")
length = len(text)
is_symmetric = True
for i in range(length):
    if text[i] != text[length - 1 - i]:
        is_symmetric = False
if is_symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")


# Q50.
text = input("Enter a string: ")
result = ""
for i in range(0, len(text), 2):
    result = result + text[i]
print(result)


# Q51.
text = input("Enter a string: ")
even_count = 0
odd_count = 0
for i in range(len(text)):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"Even Index = {even_count}, Odd Index = {odd_count}")


# Q52.
text = input("Enter an even-length string: ")
result = ""
for i in range(0, len(text), 2):
    result = result + text[i + 1] + text[i]
print(result)