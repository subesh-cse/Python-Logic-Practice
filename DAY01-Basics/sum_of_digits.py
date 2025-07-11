# Sum of Digits
# Date 2025-07-11
# Author: Subesh

num = int(input("Enter your number: "))
total = 0

while num > 0:
  total += num % 10
  num = num // 10

print("Sum of digits:", total)
