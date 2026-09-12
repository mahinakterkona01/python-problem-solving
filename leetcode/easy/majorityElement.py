"""
LeetCode 169: Majority Element
Problem Link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution :
    def majorityElement(self , nums:list[int] ) ->int:
        candidate = None
        count=0
        for num in nums :
            if count==0 :
                candidate=num
                count=1
            elif num==candidate :
                count+=1
            else :
                count-=1

        if nums.count(candidate)> len(nums)//2:
            return candidate
        else :
            return -1

if __name__=="__main__":
    sol=Solution()
    lst=[1,2,2,2,2,2,2,1,3,3,4]
    x=sol.majorityElement(lst)
    if x != -1:
        print("Majority element of the array is :", x)
    else:
        print("No majority element found.")