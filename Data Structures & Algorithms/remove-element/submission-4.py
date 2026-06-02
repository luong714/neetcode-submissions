class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        temp = []
        for index in nums:
            if index != val:
                temp.append(index)
        nums[:len(temp)] = temp
        return len(temp)