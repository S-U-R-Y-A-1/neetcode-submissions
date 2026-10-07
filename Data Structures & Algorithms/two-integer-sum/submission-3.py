class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = dict()
        for i,j in enumerate(nums):
            diff = target - j
            if diff in ans:
                return [ans[diff],i]
            ans[j] = i
        return ans
        
