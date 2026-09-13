"""
LeetCode 12: Integer to Roman
Problem Link: https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""

class Solution:
    def intToRoman(self , num:int )->str:
        value_map=[
            (1000, "M"),  (900, "CM"), (500, "D"),  (400, "CD"),
            (100, "C"),   (90, "XC"),  (50, "L"),   (40, "XL"),
            (10, "X"),    (9, "IX"),   (5, "V"),    (4, "IV"),
            (1, "I")
        ]
        result=[]
        for val, symbol in value_map :
            while num>=val :
                result.append(symbol)
                num-=val

        return "".join(result)

if __name__=="__main__":
    sol=Solution()
    x=1004
    print(sol.intToRoman(x))