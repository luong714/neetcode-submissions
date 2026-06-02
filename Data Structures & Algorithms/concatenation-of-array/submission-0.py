class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for index in range(len(ans)):
            ans.append(ans[index])
        return ans