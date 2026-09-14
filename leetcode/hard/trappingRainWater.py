"""
LeetCode 42:  Trapping Rain Water
Problem Link: https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Hard
"""
class Solution :
    def trap(self , height:list[int])->int :
        n= len(height)
        leftMax=[0]*n
        rightMax=[0]*n
        trapwater=[0]*n

        leftMax[0]=height[0]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])

        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])

        for i in range (n):
            trapwater[i]=min(leftMax[i],rightMax[i])-height[i]

        return sum(trapwater)
    
if __name__=="__main__":
    sol=Solution()
    lst=[0,1,0,2,1,0,1,3,2,1,2,1]
    x=sol.trap(lst)
    print(" total trap water : " ,x)