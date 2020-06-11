class TwoSum(object):
    def __init__(self):
        self.nums = []
        self.is_sorted = False
    def add(self, number):
        self.nums.append(number)
        self.is_sorted = False
    def find(self, value):
        if not self.is_sorted:
            self.nums.sort()
        low, high = 0, len(self.nums) - 1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else:
                return True
        return False
