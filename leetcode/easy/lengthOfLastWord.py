"""
LeetCode 58: Length of Last Word
Problem Link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""
class Solution:
    def lengthOfLastWord(self , s:str )->int :
        words=s.split()
        n=len(words)-1
        return len(words[n])

if __name__=="__main__" :
    sol=Solution()
    x="Hello this is Python Programming"
    print(" Length of last word : " , sol.lengthOfLastWord(x))