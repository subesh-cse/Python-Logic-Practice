num = int(input("Enter a number: "))
original = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print(f"The sum of digits of {original} is {sum_digits}")
