# Q15.
n = int(input("Enter N: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(factorial)


# Q16.
n = int(input("Enter N: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
    print(f"{i}! = {factorial}")


# Q17.
n = int(input("Enter N: "))
product = 1
for i in range(2, n + 1, 2):
    product = product * i
print(product)


# Q18.
n = int(input("Enter N: "))
product = 1
for i in range(1, n + 1, 2):
    product = product * i
print(product)


# Q19.
n = int(input("Enter an even number: "))
product = 1
for i in range(n, 0, -2):
    product = product * i
print(product)


# Q20.
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total = total + i ** 2
print(total)


# Q21.
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total = total + i ** 3
print(total)


# Q22.
n = int(input("Enter N: "))
factorial = 1
total = 0
for i in range(1, n + 1):
    factorial = factorial * i
    total = total + factorial
print(total)