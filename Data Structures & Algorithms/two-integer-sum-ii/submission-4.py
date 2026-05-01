class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        length = len(numbers)
        lo = 0
        hi = length - 1

        for i in range(length):
            sum_ = numbers[lo] + numbers[hi]
            if sum_ > target:
                hi -= 1
            elif sum_ < target:
                lo+=1
            elif sum_ == target:
                break
            
        return [lo+1,hi+1]

            