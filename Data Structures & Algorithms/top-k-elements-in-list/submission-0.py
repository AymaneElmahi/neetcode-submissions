class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0)+1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in frequencies.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) == k:
                return result



        

