# Q44.
a, b, c = input("Enter three numbers: ").split()
a = int(a)
b = int(b)
c = int(c)
if a == b == c:
    print("All are Equal")
elif a == b and a > c:
    print("A and B are Equal and Greatest")
elif a == c and a > b:
    print("A and C are Equal and Greatest")
elif b == c and b > a:
    print("B and C are Equal and Greatest")
elif a > b and a > c:
    print("A is Greatest")
elif b > a and b > c:
    print("B is Greatest")
else:
    print("C is Greatest")


# Q45.
marks, attendance = input("Enter marks and attendance: ").split()
marks = int(marks)
attendance = int(attendance)
if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


# Q46.
salary, rating = input("Enter salary and performance rating: ").split()
salary = int(salary)
rating = int(rating)
if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


# Q47.
age, distance = input("Enter age and distance: ").split()
age = int(age)
distance = int(distance)
if age < 5:
    print("Free")
elif age <= 59:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
else:
    print("Senior")


# Q48.
stock, payment_status = input("Enter stock and payment status: ").split()
stock = int(stock)
if stock > 0:
    if payment_status == "paid":
        print("Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Q49.
age, ticket_type = input("Enter age and ticket type: ").split()
age = int(age)
if age < 5:
    print("Free Travel")
elif age <= 59:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
else:
    print("Senior Passenger")