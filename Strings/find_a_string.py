"""
Problem: Find a String
Topics: Strings, Substrings
HackerRank: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

Approach:
- Loop through the main string and check each substring of length len(sub).
- If substring matches, increment the count.
- This correctly handles overlapping occurrences.

Time Complexity: O(n*m), where n = len(s), m = len(sub)
Space Complexity: O(1)
"""

def count_substring(s, sub):
    count = 0
    sub_len = len(sub)
    for i in range(len(s) - sub_len + 1):
        if s[i:i+sub_len] == sub:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
