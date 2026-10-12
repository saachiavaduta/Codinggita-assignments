# Q7.
start, end = input("Enter start and end: ").split()
start = int(start)
end = int(end)
total = 0
for i in range(start, end + 1):
    total = total + i
print(total)


# Q8.
n = int(input("Enter N: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count = count + 1
print(count)


# Q9.
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        total = total + i
print(total)


# Q10.
n = int(input("Enter N: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        count = count + 1
print(count)


# Q11.
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    if i % 3 != 0:
        total = total + i
print(total)


# Q12.
n = int(input("Enter N: "))
even_count = 0
odd_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"Even = {even_count}, Odd = {odd_count}")


# Q13.
n = int(input("Enter N: "))
running_sum = 0
for i in range(1, n + 1):
    running_sum = running_sum + i
    print(running_sum)


# Q14.
n = int(input("Enter N: "))
product = 1
for i in range(1, n + 1):
    product = product * i
    print(product)