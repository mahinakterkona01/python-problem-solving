"""
LeetCode 26: Remove Duplicates from Sorted Array
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""
class solution:
    def removeDuplicates (self , nums:list[int])->int:
        i=0
        for j in range(1,len(nums)) :
            if nums[i] != nums[j] :
                i+=1
                nums[i]=nums[j]
        return i+1

if __name__ == "__main__" :
    sol=solution()
    nums=[1,2,2,3,4,6,6]
    soln=sol.removeDuplicates(nums)
    print("After removing duplicate numbers from array the array becomes :",nums[:soln])