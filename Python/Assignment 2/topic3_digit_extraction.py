# Q21.
number = 583
ones_digit = number % 10
print("Ones Digit:", ones_digit)


# Q22.
number = 583
tens_digit = (number // 10) % 10
print("Tens Digit:", tens_digit)


# Q23.
number = 583
hundreds_digit = number // 100
print("Hundreds Digit:", hundreds_digit)


# Q24.
number = 746
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)


# Q25.
number = 5829
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
print("Thousands Digit:", thousands_digit)


# Q26.
number = 583
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

sum_of_digits = ones_digit + tens_digit + hundreds_digit
print("Sum of Digits:", sum_of_digits)


# Q27.
number = 4726
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

sum_of_digits = ones_digit + tens_digit + hundreds_digit + thousands_digit
print("Sum of Digits:", sum_of_digits)


# Q28.
number = 234
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

product_of_digits = ones_digit * tens_digit * hundreds_digit
print("Product of Digits:", product_of_digits)


# Q29.
number = 583
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

reversed_number = (ones_digit * 100) + (tens_digit * 10) + hundreds_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)


# Q30.
number = 4726
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

reversed_number = (ones_digit * 1000) + (tens_digit * 100) + (hundreds_digit * 10) + thousands_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)


# Q31.
number = 5834
thousands_place = (number // 1000) * 1000
hundreds_place = ((number // 100) % 10) * 100
tens_place = ((number // 10) % 10) * 10
ones_place = number % 10

print("Thousands Place:", thousands_place)
print("Hundreds Place:", hundreds_place)
print("Tens Place:", tens_place)
print("Ones Place:", ones_place)


# Q32.
number = 583
hundreds_digit = number // 100
ones_digit = number % 10

difference = hundreds_digit - ones_digit
print("Difference:", difference)


# Q33.
number = 583
ones = number % 10
print("Ones Digit:", ones)


# Q34.
number = 9365
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)


# Q35.
hundreds = 5
tens = 8
ones = 3

number = (hundreds * 100) + (tens * 10) + ones
print("Number:", number)