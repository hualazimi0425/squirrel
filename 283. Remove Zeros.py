# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeroes(self, nums: list) -> None:
    slow, fast = 0, 0
    # fast pointer track every element in the array
    # slow pointer only track non-zero element
    while fast < len(nums):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]  # swap non-zero element with zero element
        if nums[slow] != 0:
            slow += 1
        fast += 1

