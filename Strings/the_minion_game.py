"""
Problem: The Minion Game
Topics: Strings, Game Theory, Substrings
HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

Approach:
- Two players: Kevin (vowels) and Stuart (consonants).
- Each player scores points based on the number of substrings 
  starting with their assigned letters.
- Instead of generating all substrings (which is O(n^2)), 
  we can directly calculate points:
    - At index i in the string of length n, 
      the number of substrings starting at i = (n - i).
    - If s[i] is a vowel → Kevin gets (n - i) points.
    - If s[i] is a consonant → Stuart gets (n - i) points.
- After iterating, compare scores to declare the winner.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), only storing counters for scores.
"""

def minion_game(string):
    vowels = "AEIOU"
    n = len(string)
    stuart_score = 0
    kevin_score = 0
    
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
