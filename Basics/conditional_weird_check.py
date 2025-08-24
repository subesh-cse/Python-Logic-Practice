"""
Problem: Conditional Weird Check
Topics: Basics, Conditionals, Loops
HackerRank: https://www.hackerrank.com/challenges/conditional-statements/problem
Approach: 
- Read integer input
- Check for odd or even and the range conditions
- Print corresponding result
Time Complexity: O(1)
Space Complexity: O(1)
"""

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
