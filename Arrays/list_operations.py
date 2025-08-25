"""
Problem: List Operations
Topics: Lists, Arrays, Conditional Statements, Loops
HackerRank: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
Approach:
- Initialize an empty list
- Read commands and apply corresponding list operations:
    * insert i e → insert element e at index i
    * print → print the current list
    * remove e → remove first occurrence of e
    * append e → add element e to the end
    * sort → sort the list
    * pop → remove the last element
    * reverse → reverse the list
- Execute each command as it is read
Time Complexity: O(n*m) worst-case (n = number of commands, m = list length for operations like insert/remove)
Space Complexity: O(m) (size of the list)
"""

arr = []
n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        arr.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "print":
        print(arr)
    elif cmd[0] == "remove":
        arr.remove(int(cmd[1]))
    elif cmd[0] == "append":
        arr.append(int(cmd[1]))
    elif cmd[0] == "sort":
        arr.sort()
    elif cmd[0] == "pop":
        arr.pop()
    elif cmd[0] == "reverse":
        arr.reverse()
        
  
    
