"""
LeetCode 135:  Candy
Problem Link: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Hard
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        min_candy=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
               min_candy[i]=min_candy[i-1]+1

        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1]:
               min_candy[j]=max(min_candy[j],min_candy[j+1]+1)
        return sum(min_candy)

if __name__=="__main__":
    sol=Solution()
    lst=[2,0,4,5,6,7,8,9]
    x=sol.candy(lst)
    print(" Minimum Required Candy : " ,x)
