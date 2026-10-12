# Q62.
days = int(input("Enter number of days: "))
total = 0
highest = 0
lowest = 0
for i in range(days):
    expense = int(input("Enter expense: "))
    total = total + expense
    if i == 0:
        highest = expense
        lowest = expense
    else:
        if expense > highest:
            highest = expense
        if expense < lowest:
            lowest = expense
print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


# Q63.
subjects = int(input("Enter number of subjects: "))
total = 0
highest = 0
lowest = 0
for i in range(subjects):
    marks = int(input("Enter marks: "))
    total = total + marks
    if i == 0:
        highest = marks
        lowest = marks
    else:
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks
average = total / subjects
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)


# Q64.
working_days = int(input("Enter number of working days: "))
present = 0
absent = 0
for i in range(working_days):
    status = input("Enter status (P/A): ")
    if status == "P":
        present = present + 1
    else:
        absent = absent + 1
attendance = present / working_days * 100
print("Present:", present)
print("Absent:", absent)
print(f"Attendance: {attendance:.2f}%")


# Q65.
days = int(input("Enter number of days: "))
total_units = 0
days_above = 0
for i in range(days):
    units = int(input("Enter units used: "))
    total_units = total_units + units
    if units > 10:
        days_above = days_above + 1
print("Total Units:", total_units)
print("Days Above 10:", days_above)


# Q66.
products = int(input("Enter number of products: "))
total_bill = 0
above_1000 = 0
for i in range(products):
    price = int(input("Enter price: "))
    total_bill = total_bill + price
    if price > 1000:
        above_1000 = above_1000 + 1
print("Total Bill:", total_bill)
print("Products Above 1000:", above_1000)


# Q67.
attempts = int(input("Enter number of attempts: "))
successful = 0
failed = 0
for i in range(attempts):
    result = input("Enter attempt result (success/failed): ")
    if result == "success":
        successful = successful + 1
    else:
        failed = failed + 1
success_rate = successful / attempts * 100
print("Successful:", successful)
print("Failed:", failed)
print(f"Success Rate: {success_rate}%")