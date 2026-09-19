# Q56.
student_name = "Ravi"
marks = "85"

total = int(marks) + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))


# Q57.
number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)


# Q58.
price = int("2000")
discount = int("15")

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)


# Q59.
student_name = "Rahul"
marks1 = int("85")
marks2 = int("90")
marks3 = int("78")

total = marks1 + marks2 + marks3
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))


# Q60.
# Part A - Number Analysis
number = 5836

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + ones_digit
reversed_number = (ones_digit * 1000) + (tens_digit * 100) + (hundreds_digit * 10) + thousands_digit

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

# Part B - Product Billing
price = int("1250")
quantity = int("4")
discount = int("10")

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)