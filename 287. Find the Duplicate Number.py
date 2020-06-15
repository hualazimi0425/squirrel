class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lookup = set()
        for i in range(n):
            if nums[i] not in lookup:
                lookup.add(nums[i])
            else:
                return nums[i]
