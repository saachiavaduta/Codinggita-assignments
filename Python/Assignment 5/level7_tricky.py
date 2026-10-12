# Q53.
number = int(input("Enter a number: "))
temp = number
largest = -1
second_largest = -1
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            second_largest = largest
            largest = digit
        elif digit != largest and digit > second_largest:
            second_largest = digit
        temp = temp // 10
print(second_largest)


# Q54.
text = input("Enter a string: ")
current_count = 1
best_count = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current_count = current_count + 1
    else:
        current_count = 1
    if current_count > best_count:
        best_count = current_count
print(best_count)


# Q55.
text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0
for ch in text:
    if ch == target:
        count = count + 1
frequency = round(count / len(text) * 100, 2)
print(f"Count = {count}, Frequency = {frequency}%")


# Q56.
number = int(input("Enter a number: "))
temp = number
running_sum = 0
for i in range(number):
    if temp > 0:
        running_sum = running_sum + temp % 10
        print(running_sum)
        temp = temp // 10


# Q57.
number = int(input("Enter a number: "))
temp = number
even_count = 0
odd_count = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        temp = temp // 10
if even_count > odd_count:
    print("More Even Digits")
elif odd_count > even_count:
    print("More Odd Digits")
else:
    print("Equal")


# Q58.
number = int(input("Enter a number: "))
temp = number
total = 0
sign = 1
for i in range(number):
    if temp > 0:
        total = total + sign * (temp % 10)
        sign = -sign
        temp = temp // 10
print(total)


# Q61.
total = 0
for i in range(1, 6):
    total = total + i
print(total)