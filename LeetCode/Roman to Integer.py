# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        #we take two numbers at a time
        #if the second number is larger than the first number, we'll subtract from net value
        #if the first number is larger than second, we'll add it
        for a,b in zip(s,s[1:]):
            if roman[a] < roman[b]:
                value -= roman[a]
            else:
                value += roman[a]
        #since the last number will not be set as "a" in the for loop because "b"
        #will be out of bounds, we need to add it to the net result
        #We'll always add it regardless of the number, if it's smaller than the
        #previous number, we add anyways
        #If it's larger, there is no next number to compare, so that's a standalone
        #So, we always add.
        return value+roman[s[-1]]