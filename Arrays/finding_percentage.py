"""
Problem: Finding the Percentage
Topics: Dictionaries, Strings, Math
HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
Approach:
- Store student names and their marks in a dictionary
- Retrieve the marks of the queried student
- Compute average = sum(marks)/len(marks)
- Print result formatted to 2 decimal places
Time Complexity: O(n)  # for storing data and computing average
Space Complexity: O(n)  # dictionary storing all students
"""

n = int(input())
student_marks = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float,data[1:]))
    student_marks[name] = marks
    
query_name = input().strip()
avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avg_score:.2f}")

