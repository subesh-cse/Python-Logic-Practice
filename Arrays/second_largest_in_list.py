"""
Problem: Find Second Maximum Number in a List
Topics: Arrays, Lists, Sorting
HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Approach:
- Convert list to set to remove duplicates
- Check if at least 2 unique numbers exist
- Sort the unique numbers and return the second largest
Time Complexity: O(n log n)
Space Complexity: O(n)
"""


n = int(input())
arr = list(map(int,input().split()))

unique = list(set(arr))

if len(unique) < 2:
    print("No second largest")
else:
    unique.sort()
    print(unique[-2])
    
