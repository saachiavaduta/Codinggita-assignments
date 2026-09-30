# Q58.
student_id = input("Enter student ID: ")
degree, batch, branch, roll_number = student_id.split("-")
if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


# Q59.
email = input("Enter email address: ")
username, domain = email.split("@")
if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")


# Q60.
full_name = input("Enter full name: ")
first_name, middle_name, last_name = full_name.split()
generated_username = first_name.lower() + "." + last_name.lower()
if "." in generated_username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")


# Q61.
number = input("Enter a positive integer: ")
length = len(number)
if length == 1:
    print("One Digit")
elif length == 2:
    print("Two Digits")
elif length == 3:
    print("Three Digits")
else:
    print("Four or More Digits")


# Q62.
price, quantity = input("Enter price and quantity: ").split()
price = float(price)
quantity = int(quantity)
subtotal = price * quantity

if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0

discount_amount = subtotal * discount_percent / 100
final_amount = subtotal - discount_amount

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_percent}%")
print(f"Final: {final_amount:.2f}")


# Q63.
units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate

print(f"Units: {units}")
print(f"Rate: {rate}")
print(f"Bill: {bill}")


# Q64.
balance = 10000
choice = int(input("Enter choice (1-Balance, 2-Deposit, 3-Withdraw, 4-Exit): "))

match choice:
    case 1:
        print("Balance:", balance)
    case 2:
        deposit_amount = int(input("Enter deposit amount: "))
        balance = balance + deposit_amount
        print("Deposit Successful, Balance:", balance)
    case 3:
        withdraw_amount = int(input("Enter withdrawal amount: "))
        if withdraw_amount <= balance:
            balance = balance - withdraw_amount
            print("Withdrawal Successful, Balance:", balance)
        else:
            print("Insufficient Balance")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")


# Q65.
menu_choice = int(input("Enter item number (1-Pizza, 2-Burger, 3-Pasta, 4-Sandwich): "))
quantity = int(input("Enter quantity: "))

match menu_choice:
    case 1:
        price = 250
    case 2:
        price = 150
    case 3:
        price = 200
    case 4:
        price = 120
    case _:
        price = 0

total = price * quantity

if total >= 500:
    discount = total * 10 / 100
else:
    discount = 0

final_total = total - discount

print(f"Total: {total}")
print(f"Discount: {discount:.2f}")
print(f"Final: {final_total:.2f}")


# Q66.
marks1, marks2, marks3, attendance = input("Enter three marks and attendance: ").split()
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
attendance = int(attendance)

total = marks1 + marks2 + marks3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


# Q67.
distance, ride_type = input("Enter distance and ride type: ").split()
distance = int(distance)

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0

fare = distance * rate

if distance > 20:
    fare = fare + fare * 10 / 100

print(f"Fare: {fare:.2f}")


# Q68.
score, percentage, category = input("Enter entrance score, percentage and category: ").split()
score = int(score)
percentage = float(percentage)

match category:
    case "general":
        if score >= 80 and percentage >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "obc":
        if score >= 70 and percentage >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "sc":
        if score >= 60 and percentage >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case _:
        print("Invalid Category")