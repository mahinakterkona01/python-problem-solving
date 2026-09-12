"""
LeetCode 55: Jump Game
Problem Link: https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""
class Solution :
    def jumpGame(self , nums:List[int]) -> bool:
        max_reach=0
        for i in range(len(nums)) :
            if i>max_reach :
                return False
            max_reach=max(max_reach,i+nums[i])
            if max_reach>=len(nums)-1 :
                return True 
        return True
if __name__ == "__main__":
    sol=Solution()
    list=[1,1,1,2,2,2,3,3,3,3,4,5,6]
    print(sol.jumpGame(list))