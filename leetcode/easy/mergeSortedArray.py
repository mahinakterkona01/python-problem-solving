"""
LeetCode 88: Merge Sorted Array
Problem Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution :
    def mergeArray(self , nums1:list[int] , m:int , nums2:list[int] , n:int )->None :
        merged=nums1[:m]+nums2
        merged.sort()
        nums1[:]=merged

if __name__=="__main__":
    sol=Solution()
    lst1=[1,2,3,4,0,0]
    lst2=[3,4,5]
    sol.mergeArray(lst1,4,lst2,3)
    print(lst1)