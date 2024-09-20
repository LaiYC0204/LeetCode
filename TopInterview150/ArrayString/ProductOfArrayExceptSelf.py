# 暴力解
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result

# GPT講解自己寫
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        left_product = [1]
        right_product = 1
        for left in range(len(nums) - 1):
            left_product.append(left_product[left] * nums[left])

        for right in range(len(nums) - 1, -1, -1):
            result.insert(0, right_product * left_product[right])
            right_product = right_product * nums[right]

        return result

# GPT再次講解自己寫
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for _ in range(len(nums))]
        right_product = 1
        for left in range(1, len(nums)):
            result[left] = result[left - 1] * nums[left - 1]

        for right in range(len(nums) - 1, -1, -1):
            result[right] = right_product * result[right]
            right_product = right_product * nums[right]

        return result
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))