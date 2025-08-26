"""
Problem: Mutations
Topics: Strings, String Slicing
HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

Approach:
- Strings in Python are immutable, so we cannot directly change a character.
- Use slicing:
  * Take the substring before the target position.
  * Add the new character.
  * Add the substring after the position.
- Return the new string.

Time Complexity: O(n), where n is the length of the string (due to slicing).
Space Complexity: O(n), since a new string is created.
"""

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

