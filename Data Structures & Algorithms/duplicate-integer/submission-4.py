class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for i in nums:
            if exists.get(i) != None:
                return True
            exists[i] = 1
            
        return False