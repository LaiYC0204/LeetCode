# Kadane's Algorithm
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currentMaxSum, globalMaxSum = nums[0], nums[0]
    for num in nums[1:]:
        if currentMaxSum + num > num:
            currentMaxSum += num
        else:
            currentMaxSum = num

        if globalMaxSum < currentMaxSum:
            globalMaxSum = currentMaxSum

    return globalMaxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))