"""
Problem: String Validators
Topics: Strings, Character Checking, Loops
HackerRank: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

Approach:
- Iterate through the string and use Python’s built-in string methods:
  * any(c.isalnum() for c in s)
  * any(c.isalpha() for c in s)
  * any(c.isdigit() for c in s)
  * any(c.islower() for c in s)
  * any(c.isupper() for c in s)
- Print results in order as per problem requirement.

Time Complexity: O(n), where n = length of the string (single pass).
Space Complexity: O(1)
"""

def string_validators(s: str) -> None:
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper()for c in s))




if __name__ == '__main__':
    s = input()
    string_validators(s)
   
