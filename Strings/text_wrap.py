"""
Problem: Text Wrap
Topics: Strings, Text Manipulation, Python Modules
HackerRank: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
Approach:
- Use the textwrap module to handle line breaking automatically.
- textwrap.fill(string, max_width) breaks the input string into multiple lines,
  each having at most max_width characters.
- Return the resulting formatted string.
Time Complexity: O(n), where n is the length of the input string (each character is processed once)
Space Complexity: O(n), for storing the wrapped string with newlines
"""

import textwrap

def wrap(string, max_width):
    result = textwrap.fill(string, max_width)
    
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
