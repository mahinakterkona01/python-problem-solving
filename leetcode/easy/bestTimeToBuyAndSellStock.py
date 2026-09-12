"""
LeetCode 121: Best Time to Buy and Sell Stock
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""
class Solution :
    def sell_stock(self , prices:list[int] )->int :
        min_price=prices[0]
        max_profit=0
        for price in prices :
            min_price=min(min_price,price)
            max_profit=max(max_profit,price-min_price)
        return max_profit
if __name__=="__main__":
    sol=Solution()
    lst1=[1,2,6,32,4,3,7,1,3,2,1]
    x=sol.sell_stock(lst1)
    print("Maximum Profit : ",x)
