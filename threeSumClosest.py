#雙指針，跟threeSum不同不能跳過一樣的數字
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    min_gap = float('inf') #正無限大
    output = 0

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            gap = abs(target - three_sum)
            if gap < min_gap:
                output = three_sum
                min_gap = gap
            if three_sum < target:
                left += 1
            elif three_sum > target:
                right -= 1
            else:
                return three_sum #如果和target一樣那就是最佳答案

    return output

print(threeSumClosest([-1000,-1000,-1000], 10000))