class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # [[], [], [], ...]
        freq = [[] for i in range(len(nums)+1)]
        # {value: count}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        #   cnt1    cnt2    cnt3
        # [[num1], [num2], [num3], ...]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # reverse down for top to bottom
        for i in range(len(freq) - 1, 0, -1):
            # get every number in each 2D list
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    # [val1, val2, ...]
                    return res
            