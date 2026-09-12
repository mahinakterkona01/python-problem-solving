"""
LeetCode 189: Rotate Array
Problem Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""
class Solution :
    def rotateArray(self , nums:list[int] , k:int)->int:
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums

if __name__=="__main__":
    sol=Solution()
    lst=[2,3,4,5,6,7,12,23,45]
    x=sol.rotateArray(lst,4)
    print("Rotate Array :",x)