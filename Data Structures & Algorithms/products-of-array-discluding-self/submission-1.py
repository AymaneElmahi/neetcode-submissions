class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_products = [1]*len(nums)
        right_products = [1]*len(nums)
        left_total = 1
        right_total = 1
        for i in range(1,len(nums)):
            left_total = left_total * nums[i-1]
            right_total = right_total * nums[len(nums)-i]
            left_products[i] = left_total
            right_products[i] = right_total

            
        return [left_products[i]*right_products[len(nums)-i-1] for i in range(len(nums))]

