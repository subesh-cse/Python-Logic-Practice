"""
Problem: Nested Lists - Find Students with the Second Lowest Score
Topics: Lists, Sorting, Nested Structures
HackerRank: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Approach:
- Store names and scores in a nested list
- Extract unique scores and sort them
- Find the second lowest score
- Collect all student names with that score
- Sort names alphabetically and print them
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])
    
scores = sorted({s[1]for s in students})
second_lowest = scores[1]

result = [s[0] for s in students if s[1] == second_lowest]
result.sort()

for name in result:
    print(name)
