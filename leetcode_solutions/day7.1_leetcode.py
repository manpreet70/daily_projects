class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        run_total = 0
        i = 0
        n = len(s)

        while i < n:
            v = roman_val[s[i]]
            if i + 1 < n and roman_val[s[i+1]] > v:
                    run_total += roman_val[s[i+1]] - v
                    i +=2
            else:
                run_total += v
                i += 1

        return run_total
  
# First version(above): skips ahead 2 positions for subtractive pairs (while-loop).
# Second version(below): uses add/subtract logic on each char, then adds last symbol (for-loop).


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        run_total = 0
        
        for i in range(len(s)-1):
            if roman_val[s[i]] < roman_val[s[i+1]]:
                run_total -= roman_val[s[i]]
            else:
                run_total += roman_val[s[i]]
        
        run_total += roman_val[s[-1]]
        return run_total

        