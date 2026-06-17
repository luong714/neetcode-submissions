# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i-1
            while j>=0 and pairs[j].key > pairs[j+1].key:
                pairs[j+1], pairs[j] = pairs[j] , pairs[j+1]
               
                j -=1
            res.append(pairs[:])
        return res