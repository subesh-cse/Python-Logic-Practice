"""
Problem: Leap Year Check
Topics: Basics, Conditionals
HackerRank: https://www.hackerrank.com/challenges/write-a-function/problem
Approach:
- Check if year is divisible by 4 and not divisible by 100 OR divisible by 400
- Return True if leap year, False otherwise
Time Complexity: O(1)
Space Complexity: O(1)
"""

def is_leap(year):
    
    if (year % 4 == 0 and year % 100 != 0):
         leap = True 
    elif (year % 400 == 0) :
        leap = True 
    else:
        leap = False
            
    
        
    return leap

year = int(input())
print(is_leap(year))
