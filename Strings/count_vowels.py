text = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {count}")
