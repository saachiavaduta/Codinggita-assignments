# Q19.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


# Q20.
temperature = int(input("Enter temperature: "))
if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")


# Q21.
signal = input("Enter signal color: ")
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# Q22.
units = int(input("Enter electricity units: "))
if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")


# Q23.
age = int(input("Enter age: "))
if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")


# Q24.
bmi = float(input("Enter BMI: "))
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")


# Q25.
month = int(input("Enter month number: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 Days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")


# Q26.
num1, num2, operator = input("Enter two numbers and an operator: ").split()
num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")


# Q27.
day = int(input("Enter day number: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")


# Q28.
score = int(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
else:
    print("Needs Improvement")