# Q23.
number = int(input("Enter a number: "))
temp = number
count = 0
for i in range(number):
    if temp > 0:
        count = count + 1
        temp = temp // 10
print(count)


# Q24.
number = int(input("Enter a number: "))
temp = number
total = 0
for i in range(number):
    if temp > 0:
        total = total + temp % 10
        temp = temp // 10
print(total)


# Q25.
number = int(input("Enter a number: "))
temp = number
product = 1
for i in range(number):
    if temp > 0:
        product = product * (temp % 10)
        temp = temp // 10
print(product)


# Q26.
number = int(input("Enter a number: "))
temp = number
count = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            count = count + 1
        temp = temp // 10
print(count)


# Q27.
number = int(input("Enter a number: "))
temp = number
total = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            total = total + digit
        temp = temp // 10
print(total)


# Q28.
number = int(input("Enter a number: "))
temp = number
largest = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        temp = temp // 10
print(largest)


# Q29.
number = int(input("Enter a number: "))
temp = number
smallest = 9
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit < smallest:
            smallest = digit
        temp = temp // 10
print(smallest)


# Q30.
number = int(input("Enter a number: "))
temp = number
reversed_number = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp = temp // 10
print(reversed_number)


# Q31.
number = int(input("Enter a number: "))
temp = number
reversed_number = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp = temp // 10
if number == reversed_number:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q32.
number = int(input("Enter a number: "))
target = int(input("Enter target digit: "))
temp = number
count = 0
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit == target:
            count = count + 1
        temp = temp // 10
print(count)


# Q33.
number = int(input("Enter a number: "))
temp = number
for i in range(number):
    if temp >= 10:
        temp = temp // 10
print(temp)


# Q34.
number = int(input("Enter a number: "))
temp = number
largest = 0
smallest = 9
for i in range(number):
    if temp > 0:
        digit = temp % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        temp = temp // 10
print(largest - smallest)


# Q35.
number = int(input("Enter a number: "))
temp = number
position = 1
for i in range(number):
    if temp > 0:
        print(temp % 10, position)
        position = position + 1
        temp = temp // 10


# Q36.
number = int(input("Enter a 3-digit number: "))
temp = number
armstrong_sum = 0
for i in range(3):
    digit = temp % 10
    armstrong_sum = armstrong_sum + digit ** 3
    temp = temp // 10
if armstrong_sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")