"""
LeetCode 274:  H-Index
Problem Link: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""
class Solution :
    def hIndex (self , citations:list[int])->int :
        h_index=0
        n=len(citations)
        citations.sort()

        for i in range(n):
            h=n-i
            if citations[i]>=h :
                h_index=h
                break
        return h_index

if __name__=="__main__":
    sol=Solution()
    lst=[2,0,4,5,6,7,8,9]
    x=sol.hIndex(lst)
    print("H index : " ,x)
