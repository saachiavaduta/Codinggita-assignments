# Q36.
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)


# Q37.
length = 15
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


# Q38.
pi = 3.14
radius = 7

area = pi * radius ** 2
print("Area:", area)


# Q39.
celsius = 35
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)


# Q40.
total_seconds = 367
minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)


# Q41.
total_seconds = 7384
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# Q42.
basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)


# Q43.
distance = 120
mileage = 20
fuel_price = 100

fuel_required = distance / mileage
total_fuel_cost = fuel_required * fuel_price

print("Fuel Required:", fuel_required)
print("Total Fuel Cost:", total_fuel_cost)


# Q44.
price = "2500"
discount = "10"

price = int(price)
discount = int(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)