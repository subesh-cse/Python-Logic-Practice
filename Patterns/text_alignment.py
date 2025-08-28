"""
Problem: Text Alignment (H-Logo)
Topics: Strings, Loops, Nested Loops, String Formatting
HackerRank: https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
Approach:
- Break the pattern into 5 parts: Top Cone, Top Pillars, Middle Belt, Bottom Pillars, Bottom Cone
- Use string multiplication ('H'*n) to build blocks of Hs
- Use string alignment methods: .rjust(), .ljust(), .center() to position each block correctly
- Use for-loops to repeat rows and build shapes incrementally
- Dry run with small thickness values to verify alignment
Time Complexity: O(n^2), where n is the thickness (nested loops for pattern)
Space Complexity: O(1) extra space (just strings for printing)
"""

# Enter thickness (must be an odd number)
thickness = int(input())  # Example: 5
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
