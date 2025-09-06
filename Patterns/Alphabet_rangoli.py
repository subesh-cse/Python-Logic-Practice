"""
Problem: Alphabet Rangoli
Topics: Strings, Patterns, Loops
HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
Approach:
- Use a loop to generate the top half of the rangoli by slicing the alphabet string.
- Reverse the slice and append the rest to get the mirrored pattern.
- Join the letters with '-' and center them using str.center() for proper width.
- Print the middle row (the widest) and mirror the top half to create the bottom half.
Time Complexity: O(N^2), where N is the size of the rangoli (nested loops for each row and string concatenation)
Space Complexity: O(N^2), for storing each row string temporarily
"""

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    width = 4*size - 3
    rows = []

    # Top half
    for i in range(size):
        s = alphabet[size-i-1 : size]
        row = '-'.join(s[::-1] + s[1:])
        rows.append(row.center(width, '-'))

    # Print top half
    for row in rows:
        print(row)
    # Print bottom half (mirror)
    for row in reversed(rows[:-1]):
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
