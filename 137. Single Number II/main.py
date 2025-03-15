from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for val , count in frequency.items():
            if count == 1:
                return val
                break