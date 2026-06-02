class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxlen = max(maxlen , count)
                count = 0
            else:
                count += 1
        maxlen = max(maxlen , count)
        return maxlen