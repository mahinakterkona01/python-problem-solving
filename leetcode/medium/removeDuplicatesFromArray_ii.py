"""
LeetCode 80: Remove Duplicates from Sorted Array II
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""

class Solution :
    def removeDuplicates(self , nums:list[int])->int :
        i=2
        for j in range(2,len(nums)) :
            if nums[i-2]!=nums[j] :
                nums[i]=nums[j]
                i+=1
        return i 

if __name__ == "__main__":
    sol=Solution()
    list=[1,1,1,2,2,2,3,3,3,3,4,5,6]
    x=sol.removeDuplicates(list)
    print("Array :" , list[:x])