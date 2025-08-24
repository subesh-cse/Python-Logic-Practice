"""
Problem: List Comprehension Combinations
Topics: Loops, List Comprehension, Nested Loops
HackerRank: https://www.hackerrank.com/challenges/list-comprehensions/problem
Approach:
- Generate all possible [i, j, k] combinations within given ranges
- Include only combinations where sum != n
Time Complexity: O(x * y * z)
Space Complexity: O(x * y * z)
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())


result = [[i,j,k]
for i in range(x + 1)
for j in range(y+1)
for k in range(z+1)
if i + j + k != n]

print(result)
