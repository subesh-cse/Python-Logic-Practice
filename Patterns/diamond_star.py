rows = int(input("Enter an odd number for rows: "))
for i in range(1, rows + 1, 2):
    print(" " * ((rows - i)//2) + "*" * i)
for i in range(rows - 2, 0, -2):
    print(" " * ((rows - i)//2) + "*" * i)
