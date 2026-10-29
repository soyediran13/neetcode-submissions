class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     prevnum = {}

     for index, value in enumerate(nums):
        diff = target - value
        if diff in prevnum:
            return [prevnum[diff], index]
        prevnum[value] = index