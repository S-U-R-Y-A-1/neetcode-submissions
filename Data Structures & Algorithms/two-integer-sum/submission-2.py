class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = dict()
        for i,j in enumerate(nums):
            difference = target - j
            if j in ans:
                return [ans[j],i]
            ans[difference] = i
        
