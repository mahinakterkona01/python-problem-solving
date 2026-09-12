"""
LeetCode 45: Jump Game II
Problem Link: https://leetcode.com/problems/jump-game-ii/
Difficulty: Medium
"""
class Solution :
    def jumpGame(self , nums:List[int]) -> bool:
        jump=0
        max_reach=0
        current_end=0
        for i in range(len(nums)) :
            max_reach=max(max_reach,i+nums[i])
            if i==current_end :
                jump+=1
                current_end=max_reach
                
        return jump
if __name__ == "__main__":
    sol=Solution()
    list=[1,1,1,2,2,2,3,3,3,3,4,5,6]
    print(sol.jumpGame(list))