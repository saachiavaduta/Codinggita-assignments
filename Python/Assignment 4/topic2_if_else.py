# Q9.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q10.
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q11.
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q12.
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Non-Positive")


# Q13.
number = int(input("Enter a number: "))
if number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Q14.
correct_password = "python123"
password = input("Enter password: ")
if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")


# Q15.
username = input("Enter username: ")
if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")


# Q16.
num1, num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)
if num1 == num2:
    print("Both are Equal")
elif num1 > num2:
    print(num1)
else:
    print(num2)


# Q17.
temperature = int(input("Enter temperature: "))
if temperature > 30:
    print("Hot")
else:
    print("Comfortable")


# Q18.
amount = int(input("Enter shopping amount: "))
if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")