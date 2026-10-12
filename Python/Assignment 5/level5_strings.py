# Q37.
text = input("Enter a string: ")
for i in range(len(text)):
    print(i, text[i])


# Q38.
text = input("Enter a string: ")
count = 0
for ch in text:
    count = count + 1
print(count)


# Q39.
text = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in text:
    if ch != " ":
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print(f"Vowels = {vowels}, Consonants = {consonants}")


# Q40.
text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0
for ch in text:
    if ch == target:
        count = count + 1
print(count)


# Q41.
text = input("Enter a string: ")
target = input("Enter target character: ")
position = -1
for i in range(len(text)):
    if text[i] == target and position == -1:
        position = i
if position == -1:
    print("Not Found")
else:
    print(position)


# Q42.
text = input("Enter a string: ")
uppercase = 0
lowercase = 0
for ch in text:
    if ch >= "A" and ch <= "Z":
        uppercase = uppercase + 1
    elif ch >= "a" and ch <= "z":
        lowercase = lowercase + 1
print(f"Uppercase = {uppercase}, Lowercase = {lowercase}")


# Q43.
text = input("Enter a string: ")
for ch in text:
    print(ch, ord(ch))


# Q44.
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in "aeiouAEIOU":
        result = result + ch
print(result)