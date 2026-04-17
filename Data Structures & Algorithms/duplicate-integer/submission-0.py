class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        count = 0
        for n in nums:
            if n in freq:
                freq[n] += 1
                return True
            else: 
                freq[n] = 1
        return False