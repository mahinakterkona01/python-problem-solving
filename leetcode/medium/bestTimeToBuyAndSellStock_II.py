"""
LeetCode 122: Best Time to Buy and Sell Stock II
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""
class Solution:
    def maxProfit(self , prices:list[int] )->int:
        totalProfit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                totalProfit+=prices[i+1]-prices[i]
        return totalProfit
if __name__=="__main__":
    sol=Solution()
    lst=[2,3,1,5,1,6,2,7,3,4,3,3,3]
    x=sol.maxProfit(lst)
    print("Maximum Profit : " , x)