class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
            
        full_product = 1
        non_null_product = 1

        for num in nums:
            if num !=0:
                non_null_product = non_null_product * num
            full_product = full_product * num
        
        if full_product == 0:
            return [non_null_product if num == 0 else 0 for num in nums ]
        
        return [full_product//num for num in nums]