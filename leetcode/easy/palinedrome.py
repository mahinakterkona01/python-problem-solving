"""
LeetCode 9: Palindrome Number
Problem Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    sol = Solution()
    
    # Test Cases
    print(sol.isPalindrome(121))   # Expected Output: True
    print(sol.isPalindrome(-121))  # Expected Output: False
    print(sol.isPalindrome(10))    # Expected Output: False