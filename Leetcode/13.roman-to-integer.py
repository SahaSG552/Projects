#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {"I": 1,
                         "V": 5,
                         "X": 10,
                         "L": 50,
                         "C": 100,
                         "D": 500,
                         "M": 1000
                         }
        calc = 0
        i = 0
        while i < len(s):
            if s[i] == "I" and len(s) - i > 1:
                if s[i+1] == "V":
                    calc += 4
                    i += 2
                elif s[i+1] == "X":
                    calc += 9
                    i += 2
                else:
                    calc += roman_numbers[s[i]]
                    i += 1

            elif s[i] == "X" and len(s) - i > 1:
                if s[i+1] == "L":
                    calc += 40
                    i += 2
                elif s[i+1] == "C":
                    calc += 90
                    i += 2
                else:
                    calc += roman_numbers[s[i]]
                    i += 1
            elif s[i] == "C" and len(s) - i > 1:
                if s[i+1] == "D":
                    calc += 400
                    i += 2
                elif s[i+1] == "M":
                    calc += 900
                    i += 2
                else:
                    calc += roman_numbers[s[i]]
                    i += 1
            else:
                calc += roman_numbers[s[i]]
                i += 1

        return calc

# @lc code=end
