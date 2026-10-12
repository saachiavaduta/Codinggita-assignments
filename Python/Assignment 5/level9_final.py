# Q68.
number = int(input("Enter a number: "))
temp = number
digit_count = 0
digit_sum = 0
largest = 0
smallest = 9
even_count = 0
odd_count = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        digit_count = digit_count + 1
        digit_sum = digit_sum + digit
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        if digit % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        temp = temp // 10
print("Digits:", digit_count)
print("Sum:", digit_sum)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even_count)
print("Odd Digits:", odd_count)


# Q69.
text = input("Enter a string: ")
total_chars = len(text)
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index_chars = 0
for i in range(len(text)):
    ch = text[i]
    if i % 2 == 0:
        even_index_chars = even_index_chars + 1
    if ch != " ":
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
        if ch >= "A" and ch <= "Z":
            uppercase = uppercase + 1
        elif ch >= "a" and ch <= "z":
            lowercase = lowercase + 1
print("Total Characters:", total_chars)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index_chars)