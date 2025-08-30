"""
Problem: Designer Door Mat
Topics: Loops, Patterns, Strings
HackerRank: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
Approach:
- Read n (rows) and m (columns) from input.
- Top half: loop i from 0 to n//2 - 1
    - Create pattern '.|.' repeated (2*i + 1) times
    - Center it within width m using '-'
- Middle: print 'WELCOME' centered in width m
- Bottom half: loop i from n//2 -1 down to 0
    - Mirror the top half using same pattern logic
Time Complexity: O(n*m), each row is processed to center the string
Space Complexity: O(1), extra space is negligible except for temporary pattern strings
"""

if __name__ == '__main__':
    n, m  = map(int, input().split())

    for i in range(n//2):
        pattern = ".|." * (2*i + 1)
        print(pattern.center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n//2-1, -1, -1):
        pattern = ".|." * (2*i + 1)
        print(pattern.center(m, "-")

