"""
LeetCode 27: Remove Element
Problem Link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution:
    def remove_element(self , nums:list[int] , val:int)->int :
        i=0
        for j in range(len(nums)) :
            if val!=nums[j] :
                nums[i]=nums[j]
                i+=1

        return i

if __name__ == "__main__" :
    sol=Solution()
    lst=[1,2,3,4,2,6,7]
    x=sol.remove_element(lst,2)
    print(f"Output array : {lst[:x]}")