"""
Problem: String Formatting
Topics: Strings, Number Systems, Formatting
HackerRank: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
Approach:
- Determine the width of the binary representation of n.
- Iterate from 1 to n and for each number:
  - Convert to decimal, octal, hexadecimal (uppercase), and binary.
  - Right-align each value based on the width.
- Print all four values on the same line, separated by a space.
Time Complexity: O(n) where n is the input number.
Space Complexity: O(1) extra space (ignoring output storage).
"""

def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate the width based on binary representation

    for i in range(1, number + 1):
        # Format each value to the calculated width
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
