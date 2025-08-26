"""
Problem: String Split and Join
Topics: Strings, Split, Join
HackerRank: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
Approach:
- Read the input string.
- Split the string into a list of words using split(" ").
- Join the words back together with "-" as the separator.
- Return and print the modified string.
Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(n) for storing the split list.
"""

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()  # Read input string
    result = split_and_join(line)
    print(result)
