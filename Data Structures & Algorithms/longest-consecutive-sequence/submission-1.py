class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        roots = {}
        for num in nums:
            if num - 1 not in set_nums:
                roots[num] = 1

        for root in roots.keys():
            length = 1
            while root + length in set_nums:
                length += 1
            roots[root] = length
        
        return max(roots.values(), default=0)


        
                
